import math
#zad1
# with open('tekst.txt', 'r', encoding='utf8') as file:
#     zawartosc = file.read()
#     znaki = zawartosc[71:111]
#     duze_a = [x for x in znaki if x.isupper()]
#     if duze_a.count('A') == 0:
#         print('Fragment tekstu nie zawiera liter "A"')
#     else:
#         print(f'Fragment tekstu zawiera literę "A" {len(duze_a)} razy.')

#zad2
# lista1 = [2, 4, 6, 8, 10, 2.5, 4.5, 6.5, 10.5]
# lista2 = [x for x in lista1 if isinstance(x, float)]
# print(lista1)
# print(lista2)

#zad3
# def suma_pierwszego_elementu(lista):
#     for i in range(len(lista)):
#         lista.append(lista[0] + lista[i])
#     return lista
#
# lista = [2, 4, 6, 8, 10]
# print(suma_pierwszego_elementu(lista))

#zad4
# a = math.sin(56)**2 + ((4**2/25) + math.log(85, 3))**(1/4)
# print(f'Wynik wynosi {a:.2f}')

#zad5
# n1 = input('Podaj n1: ')
# n2 = input('Podaj n2: ')
# try:
#     n1 = int(n1)
#     n2 = int(n2)
#     suma = sum(range(n1, n2+1))
#     with open('zadanie5.txt', 'w') as file:
#         file.write(str(suma))
# except ValueError:
#     print('Podałeś złe wartości')

