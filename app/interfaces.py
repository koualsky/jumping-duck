from abc import ABC, abstractmethod


class DuckInterface(ABC):
    @abstractmethod
    def change_position(self, press):
        pass


class TableInterface(ABC):
    @abstractmethod
    def show_duck_position(self, duck: DuckInterface):
        pass
