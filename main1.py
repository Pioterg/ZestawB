import math
# #zad1
# a = (math.log(20) + math.cos(45) + math.exp(1))**(1/3)
# print(f'{a:.2f}')
#
# #zad 2
# lista1 = [1, 2, 3, 4, 5, 6, 7]
# lista2 = [x for x in lista1 if x > min(lista1)]
# print(lista1)
# print(lista2)
#
# #zad3
# def filtrowanie(slownik):
#     wynik = []
#     for key, value in slownik.items():
#         if isinstance(key, float) and isinstance(value, float):
#             wynik.append((key, value))
#     return wynik
# moj_slownik = {'a': 1, 'b': 2.5, 3: 4.2, 5.1: 'c', 6.2: 7.3, 'd': 1, 'e': 2.5, 3: 4.2, 5.1: 'f', 8.8: 9.4,}
# print(filtrowanie(moj_slownik))
#
# #zad4
# with open('tekst (1).txt', 'r', encoding='utf8') as file:
#     file.seek(0)
#     zawartosc = file.read()
#     znaki = zawartosc[16:57]
# print(znaki)
# male_c = [x for x in znaki if x.islower()]
# if male_c.count('c') == 0:
#     print('Fragment tekstu nie zawiera liter "c"')
# else:
#     print(f'Fragment tekstu zawiera literę "c" {len(male_c)} razy.')
#
#zad5
# try:
#     a1 = int(input('Podaj a1: '))
#     n = int(input('Podaj n: '))
#     q = int(input('Podaj q:'))
#     if n <= 0:
#         raise ValueError()
# except ValueError:
#     print('Podałeś złe wartości')
#
# else:
#     wynik = a1 * (q ** (n - 1))
#     with open('zadanie5.txt', 'w') as plik:
#         plik.write(str(wynik))
#     print(wynik)
