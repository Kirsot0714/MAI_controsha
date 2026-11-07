import math

class FebNums:

    def __init__(self, end=math.inf):
        self.start = 0
        self.end = end
        self.prev_prev = 0
        self.prev = 1

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        while self.start < self.end:
            yield self.prev_prev
            current = self.prev + self.prev_prev
            self.prev_prev = self.prev
            self.prev = current
            self.start += 1


f = FebNums(10)
for _f in f:
    print(_f)