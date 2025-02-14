# writemore

A library of customizable autonomous agents for common jobs.


## Installation

Make sure you have all the **requirements** above, if not, install/get them.

*The following commands should be executed in a CMD, Bash or Powershell window. To do this, go to a folder on your computer, click in the folder path at the top and type CMD, then press enter.*

Clone the repository and install the requirements (we recommend using a virtual environment like `conda`):

```bash
pip install -r requirements.txt
```

Rename `.env.template` to `.env` and fill in your `OPENAI_API_KEY` from the [OpenAI dashboard](https://platform.openai.com/account/api-keys).

## Usage

Run the `cli.py` python script in your terminal:
*(Type this into your CMD window)*

```bash
python cli.py
```

## Contributing

Create conda environment and install dev requirements

```bash
conda create -n writemore python=3.8
conda activate writemore
pip install -r requirements-dev.txt
```

writemore uses `pre-commit` to run code checks and tests before every commit. To install the pre-commit hooks, run the following commands:

```bash
pip install pre-commit
pre-commit install
```

## Development Roadmap

ToDos

- [ ] Add memory, expose at least one local and one thirt party API
- [ ] Expose all LangChain LLM models available
- [ ] Add at least 5 jobs, as for example: conduct market research, write an engaging linkedin, prove a simple theorem
- [ ] Interactive mode
- [ ] Localhost web-ui
- [ ] Privacy-preserving on-premise workflow (not third party APIs)
