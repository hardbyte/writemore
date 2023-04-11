from typing import Optional

import click
from pydantic import BaseSettings

from writemore.writemore import writemore


class WriteMoreCLISettings(BaseSettings):
    OPENAI_API_KEY: str

    OBJECTIVE: Optional[str]
    FIRST_TASK: Optional[str]


settings = WriteMoreCLISettings()


@click.command()
@click.option(
    "-o",
    "--objective",
    help="High level objective",
    prompt=True,
    default=lambda: settings.OBJECTIVE,
)
@click.option("--first-task", help="First task", prompt=True, default=lambda: settings.FIRST_TASK)
@click.option("-v", "--verbose", is_flag=True, help="Run in verbose mode.")
def main(objective: str, first_task: str, verbose: bool):
    print(f"Executing a plan for this objective: {objective}")
    writemore(objective, first_task, verbose)


if __name__ == "__main__":
    main()
