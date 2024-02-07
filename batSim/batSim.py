Batteries = {'Pylontech_US5000' : {'Brand' : 'Pylontech', 'type': 'US5000', 'voltage': 48, 'capacity': 4800, 'pmax': 2400, 'degradation': 0.0089}}

class batSim(object):

    def __init__(self) -> None:
        pass

class Battery(object):

    def __init__(self, batInfoDict) -> None:
        self.soc = 0
        self.Ah = 0
        self._cycles = 0
        self.__dict__.update(batInfoDict)

    @property
    def cycles(self):
        return self._cycles

    @cycles.setter
    def cycles(self, value):
        self._cycles = value


    def calc_degradation(self):
        return 100 - self.degradation * self.cycles