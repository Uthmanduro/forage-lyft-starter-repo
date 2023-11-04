from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import Battery

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return any([self.engine.needs_service(), self.battery.needs_service()])
    
    