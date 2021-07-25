import Path from pathlib

class Site:
    def __init__(self, source, dest):
        self.source = Path()
        self.dest = Path()

    def create_dir():
        directory = "{}/{}".format(self.dest, self.source.relative_to())
        directory.mkdir(parents=True, exist_ok=True)

    def build():
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                create_dir(path)
