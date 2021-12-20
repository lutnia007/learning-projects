import math

class FunkcjaKwadratowa:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        return f'{self.a}*x^2+{self.b}*x+{self.c}'

    def oblicz_wartosc(self, x):
        return x**2*self.a+x*self.b+self.c

    def rozwiaz(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta == 0:
            x0 = -self.b / (2 * self.a)
            return x0
        elif delta < 0:
            return 'brak miejsc zerowych'
        else:
            x1 = (-self.b - math.sqrt(delta)) / 2 * self.a
            x2 = (-self.b + math.sqrt(delta)) / 2 * self.a
            return x1,x2

    def przeciecieOY(self):
        return self.oblicz_wartosc(0)

def wczytaj_funkcje_kwadratowa():
    print('Podaj współczynniki funkcji kwadratowej.')
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    c = int(input('Podaj c: '))

    if a==0:
        print('Ta funkcja nie jest funkcją kwadratową.')
        wczytaj_funkcje_kwadratowa()
    else:
        func = FunkcjaKwadratowa(a,b,c)
        return func

print('Witaj w kalkulatorze funkcji kwadratowych.Podaj funkcję.\n')
func1 = wczytaj_funkcje_kwadratowa()
print('Podana została funkcja kwadratowa o wzorze: y=', func1.wypisz(), '\n')

wybor = 0

while wybor != 4:
    print('Co chcesz zrobić ze swoją funkcją?\n1.Znaleźć wartość funkcji w miejscu x.\n2.Znależć miejsca zerowe funkcji.\n3.Znaleźć miejsce przecięcia funkcji z osią OY.\n4.Wyjść z programu.')
    wybor = int(input())
    match wybor:
        case wybor if wybor == 1 :
            x = int(input('Podaj argument x: '))
            print(f'Wartość tej funkcji dla x={x}:', func1.oblicz_wartosc(x),'\n')
        case wybor if wybor == 2 :
            print('Informacje o miejscach zerowych:',func1.rozwiaz(),'\n')
        case wybor if wybor == 3:
            print('Podana funkcja przecina oś OY w punkcie: (0, ', func1.przeciecieOY(), ')\n')

print('Koniec.')
