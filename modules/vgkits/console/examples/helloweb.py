from vgkits.console.webGameConsole import hostGame
from vgkits.console.examples.helloworld import createSequence


def run():
    hostGame(createSequence)


if __name__ == "__main__":
    run()