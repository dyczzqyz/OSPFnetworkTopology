from interface import Interface

class Router:
    def __init__(self, name):
        self.name=name
        self.interfaces = list()
        self.adjacents = list()

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
