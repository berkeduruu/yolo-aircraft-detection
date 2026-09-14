# Contributing

Keep model, inference, and documentation changes focused. State the dataset split, model checkpoint, hardware, and confidence settings used for verification.

Run the hardware-independent checks before opening a pull request:

```bash
python -m compileall -q codes models
python -m pytest -q
```

Do not commit private datasets, credentials, or unreviewed model artifacts.
