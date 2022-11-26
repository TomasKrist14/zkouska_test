#!/usr/bin/env python3

class Kostka:
    """
    Třída reprezentuje hrací kostku.
    """
    
    def __init__(self, pocet_sten=6):
        self.__pocet_sten = pocet_sten

    def __str__(self):
        """
        Vrací textovou reprezentaci kostky.
        """
        return str("Kostka s {0} stěnami".format(self.__pocet_sten))

    def vrat_pocet_sten(self):
        return self.__pocet_sten

    def hod(self):
        """
        Vykoná hod kostkou a vrátí číslo od 1 do
        počtu stěn.
        """
        import random as _random
        return _random.randint(1, self.__pocet_sten)


# vytvoření
sestistenna = Kostka()
desetistenna = Kostka(10)

#hod šestistěnnou
print(sestistenna)
for _ in range(10):
    print(sestistenna.hod(), end=" ")

#hod desetistěnnou
print("\n", desetistenna, sep="")
for _ in range(10):
    print(desetistenna.hod(), end=" ")
	
input()
