from pathlib import Path

class Site:
    def __init__(self, source, dest):
        source = Path()
        dest = Path()

    def create_dir(self):
        directory = "{}/{}".format(self.dest, self.source.relative_to())
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                create_dir(self, path)
