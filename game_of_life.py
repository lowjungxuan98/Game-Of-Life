class Cell:
    def __init__(self, alive):
        self._alive = alive
        self._neighbours: int  = 0

    @property
    def neighbours(self) -> int:
        return self._neighbours

    @neighbours.setter
    def neighbours(self, value):
        pass

    def set_state(self):
        if self._alive:
            if self._neighbours < 2 or self._neighbours > 3:
                self._alive = False
        else:
            if self._neighbours == 2 or self._neighbours == 3:
                self._alive = True

