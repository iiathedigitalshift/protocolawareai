# Protocol-Aware AI

A values-shaped assistant that listens to nostr relays, scans trusted sources, and reposts content aligned with clarity, autonomy, and reflection; under your own identity.

This assistant was designed for presence, not performance. It does not reply, engage, or optimize for attention. It filters quotes and signals that resonate with its owner, then reposts them from a personal `npub`.

---

### What It Does

- Subscribes to people you follow on Nostr
- Filters for quotes by:
  - Thich Nhat Hanh
  - Desmond Tutu
  - Dr. Martin Luther King Jr.
  - Joseph Campbell
- Fetches articles from BBC on:
  - Disability inclusion
  - Mental health
- Pulls daily quotes from [plumvillage.org](https://plumvillage.org)
- Reposts qualifying content using your own Nostr identity (`nsec`)
- Quietly logs activity—no replies, DMs, or engagement

---

### How to Use

1. Install requirements:
```bash
pip install git+https://github.com/jeffthibault/python-nostr
pip install websockets requests
```

2. Set your `nsec` key in the script or via environment variable.

3. Run the bot:
```bash
python nostr_assistant_bot_full.py
```

You may customize your filters, quote sources, or posting behavior by editing the configuration section in the script.

If this feels useful, use it carefully.

---

### License
MIT License.  
