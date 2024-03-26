from abc import abstractmethod


class MusicSizes:
    @abstractmethod
    def size(self): pass


class Size2_4(MusicSizes):
    def size(self): return "2/4"


class Size4_8(MusicSizes):
    def size(self): return "4/8"


class Size3_8(MusicSizes):
    def size(self): return "3/8"


class Size4_4(MusicSizes):
    def size(self): return "4/4"


class Size3_4(MusicSizes):
    def size(self): return "3/4"


class Size6_8(MusicSizes):
    def size(self): return "6/8"


class Polka(Size2_4, Size4_8): pass


class Marsh(Size2_4, Size4_8): pass


class Sonata(Size4_4, Size3_4, Size3_8): pass


class Vals(Size3_4, Size6_8): pass


print(Sonata().size())
print(Polka().size())
