class Interface:

    def __init__(self, name, ipAddress, netmask, speed, cost):  # falta el cost
        self.name = name
        self.ipAddress = ipAddress
        self.netmask = netmask
        self.speed = speed
        self.cost = cost

    def __str__(self):
        return self.ipAddress

    def __repr__(self):
        return self.ipAddress

    def getIP(self):
        return self.ipAddress

    def getMask(self):
        return self.netmask
