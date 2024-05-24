# Text-to-Speech

To use the text-to-speech program written in Python, follow these steps:

Run the program from your terminal by executing:

```bash
python texttospeech.py
```
You can then input your desired text string interactively.

Alternatively, you can pass the text string and optionally specify a voice directly from the command line:
```bash
python texttospeech.py "your text here" [voice]
```

If you provide only the text, it will use the default voice (0, which is male).
If you specify a voice, use 0 for the default male voice or 1 for a female voice.
For example:

```bash
python texttospeech.py "This is a sample text" 1
```
