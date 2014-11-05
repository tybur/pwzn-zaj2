# -*- coding: utf-8 -*-

import math


class Integrator(object):

    """
    Klasa która implementuje całki metodą Newtona Cotesa z użyciem interpolacji
    N-tego stopnia :math:`n\in<2, 11>`.

    .. note::

        Używamy wzorów NC nie dlatego że są super przydatne (zresztą gorąco
        zniechęcam Państwa przed pisaniem własnych podstawowych algorytmów
        numerycznych --- zbyt łatwo o głupi błąd) ale dlatego żebyście
        jescze raz napisali jakiś algorytm w którym nie opłaca się zrobić 11
        ifów.

    """

    @classmethod
    def get_level_parameters(cls, level):
        """

        :param int level: Liczba całkowita większa od jendości.
        :return: Zwraca listę współczynników dla poszczególnych puktów
                 w metodzie NC. Na przykład metoda NC stopnia 2 używa punktów
                 na początku i końcu przedziału i każdy ma współczynnik 1,
                 więc metoda ta zwraca [1, 1]. Dla NC 3 stopnia będzie to
                 [1, 3, 1] itp.
        :rtype: List of integers
        """
        return self.coeffs[level]

    def __init__(self, level):
        """
        Funkcja ta inicjalizuje obiekt do działania dla danego stopnia metody NC
        Jeśli obiekt zostanie skonstruowany z parametrem 2 używa metody trapezów.
        :param level: Stopień metody NC
        """
        self.coeffs = {2: [1/2, 1/2], 3: [1/3, 4/3, 1/3], 4: [3/8, 9/8, 9/8, 3/8], 5: [14/45, 64/45, 24/45, 64/45, 14/45]}
        self.coeffs[6] = [5*x/288 for x in [19, 75, 50, 50, 75, 19]]
        self.coeffs[7] = [x/140 for x in [41, 216, 27, 272, 27, 216, 41]]
        self.coeffs[8] = [7*x/17280 for x in [751, 3577, 1323, 2989, 2989, 1323, 3577, 751]]
        self.coeffs[9] = [4*x/14175 for x in [989, 5888, -928, 10496, -4540, 10496, -928, 5888, 989]]
        self.coeffs[10] = [9*x/89600 for x in [2857, 15741, 1080, 19344, 5778, 5778, 19344, 1080, 15741, 2857]]
        self.coeffs[11] = [5*x/299376 for x in [16067, 106300, -48525, 272400, -260550, 427368, -260550, 272400, -48525, 106300, 16067]]
        self.level = level

    def integrate(self, func, func_range, num_evaluations):
        """
        Funkcja dokonuje całkowania metodą NC.

        :param callable func: Całkowana funkcja, funkcja ta ma jeden argument,
                              i jest wołana w taki sposób: `func(1.0)`.
        :param Tuple[int] func_range: Dwuelementowa krotka zawiera początek i koniec
                                 przedziału całkowania.
        :param int num_evaluations: Przybliżona lość wywołań funkcji ``func``,
            generalnie algorytm jest taki:

            1. Dzielimy zakres na ``num_evaluations/self.level`` przdziałów.
               Jeśli wyrażenie nie dzieli się bez reszty, należy wziąć najmiejszą
               liczbę całkowitą większą od `num_evaluations/self.level``. 
            2. Na każdym uruchamiamy metodę NC stopnia ``self.level``
            3. Wyniki sumujemy.

            W tym algorytmie wykonamy trochę więcej wywołań funkcji niż ``num_evaluations``,
            dokłanie ``num_evaluations`` byłoby wykonywane gdyby keszować wartości
            funkcji na brzegach przedziału całkowania poszczególnych przedziałów.

        :return: Wynik całkowania.
        :rtype: float
        """
        n = -(-num_evaluations//self.level)
        xdata = self.frange(func_range[0], func_range[1], n+1)
        integral = 0
        #dx = (func_range[1]-func_range[0])/(num_evaluations-1)
        coeffs = self.coeffs[self.level]
        for i in range(len(xdata[:-1])):
            xpoints = self.frange(xdata[i], xdata[i+1], self.level)
            dx = xpoints[1] - xpoints[0]
            integral += dx*sum([func(x)*c for x,c in zip(xpoints, coeffs)])
        return integral
    

    def frange(self, x0, xN, n):
        dx = (xN-x0)/(n-1)
        x = x0
        result = [x0]
        for i in range(1, n):
            x += dx
            result.append(x)
        return result


if __name__ == '__main__':
    i = Integrator(10)
    print(i.integrate(math.sin, (0, 2*math.pi), 30))
    print(i.integrate(lambda x: x*x, (0, 1), 30))
