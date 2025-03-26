# presence_bot.py
# A values-shaped assistant for Nostr
# Author: The Digital Shift

# Dependencies:
# pip install git+https://github.com/jeffthibault/python-nostr
# pip install websockets requests

import asyncio
import json
import time
from nostr.relay_manager import RelayManager
from nostr.message_type import ClientMessageType
from nostr.event import Event
from nostr.key import PrivateKey
from nostr.filter import Filter, Filters
from nostr.event_kind import EventKind

# ---------------------------
# CONFIGURATION
# ---------------------------
NSEC = 'your_nsec_here'  # Replace this with your nsec or use environment variable
PRIVATE_KEY = PrivateKey().from_nsec(NSEC)
PUBKEY = PRIVATE_KEY.public_key.hex()

RELAY_URLS = [
    "wss://nostr.land",
    "wss://relay.nostr.band",
    "wss://relay.damus.io",
    "wss://nos.lol"
]

QUOTE_MATCHES = [
    "thich nhat hanh",
    "desmond tutu",
    "martin luther king",
    "joseph campbell"
]

# ---------------------------
# MATCHING FUNCTION
# ---------------------------
def matches_criteria(content):
    content_lower = content.lower()
    return (
        any(author in content_lower for author in QUOTE_MATCHES)
        and not content.startswith("@")
        and content != content.upper()
    )

# ---------------------------
# BOT LOOP
# ---------------------------
async def run_bot():
    relay_manager = RelayManager()
    for relay in RELAY_URLS:
        relay_manager.add_relay(relay)
    relay_manager.open_connections({"cert_reqs": 0})
    time.sleep(1.25)

    # Historical check (last 24h)
    filters = Filters([Filter(kinds=[1], since=int(time.time()) - 86400)])
    subscription_id = "daily_check"
    request = [ClientMessageType.REQUEST, subscription_id]
    request.extend(filters.to_json_array())
    relay_manager.publish_message(json.dumps(request))

    print("Bot is live – scanning for matches...")

    while True:
        time.sleep(2)
        events = relay_manager.get_events()
        for event in events:
            content = event.content
            pubkey = event.pub_key

            if matches_criteria(content):
                print(f"Matched note from {pubkey[:10]}: \"{content[:60]}...\"")

                repost_event = Event(
                    content=content,
                    public_key=PUBKEY,
                    kind=EventKind.TEXT_NOTE
                )
                PRIVATE_KEY.sign_event(repost_event)
                relay_manager.publish_event(repost_event)

        relay_manager.clear_events()

if __name__ == "__main__":
    asyncio.run(run_bot())
