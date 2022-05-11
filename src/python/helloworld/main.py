import click

from package.utils import get_df

@click.command()
def display():
    click.echo(get_df())

if __name__ == "__main__":
    display()
