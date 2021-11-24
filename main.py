
# Zaimplementować funkcję numbers(n: int), która wypisze liczby od n do 0
# def numbers(n:int):
#     print(n)
#     if n == 0:
#         return
#
#     numbers(n - 1)
#
# numbers(25)

#--------------------------------------------------------
# Zaimplementować funkcję fib(n: int) -> int, która obliczy n-ty wyraz ciągu Fibonacciego
# def fib(n:int)-> int:
#     if n < 2 :
#         return n
#
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(29))
#

#--------------------------------------------------------
#Zaimplementować funkcję power(number: int, n: int) -> int,
# której zadaniem jest zwrócenie wyniku działania $ number^n $ NIE UŻYWAĆ OPERATORA **

# def power (number: int, n: int)->int:
#     if n < 2:
#         return number
#
#     return power(number, n - 1) + power(number, n-2)
#
# print(power(2 ,2))



#--------------------------------------------------------
# Zaimplementować funkcję reverse(txt: str) -> str, która zwróci odwrócony ciąg znaków przekazany w parametrze txt
# def reverse(txt: str) -> str:
#     if len(txt) == 0:
#         return txt
#     else:
#         return reverse(txt[1:]) + txt[0]
#
#
# a = str(input("Pisz co ma być odwrocone: "))
# print(reverse(a))


#--------------------------------------------------------
#Zaimplementować funkcję factorial(n: int) -> int, która zwróci silnię wartości przekazanej w parametrze
# def factorial(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# b = a = int(input("Podaj liczbe: "))
# print(factorial(b))



#--------------------------------------------------------
#Zaimplementować funkcję prime(n: int) -> bool, która sprawdzi,
#czy liczba podana w parametrze jest liczbą pierwszą.
#Podpowiedź: wystarczy sprawdzić czy n jest podzielne przez wszystkie liczby poprzedzające

# def prime(n: int) -> bool:
#     if n > 1:
#         for i in range(2,n):
#             if (n%i) == 0:
#                 print(n," nie jest liczba pierwsza")
#                 return
#             else:
#                 print(n," jest liczba pierwsza")
#                 return
#
#     else:
#         print(n, " nie jest liczba pierwsza")
#
# c = int(input("Podaj liczbe: "))
# print(prime(c))


# def prime(n:int, i = None) -> bool:
#     if i is None:
#         i = n - 1
#     while i>=2:
#         if n % i == 0:
#             print("Liczba nie jest pierwsza")
#             return
#         else:
#             return prime(n,i-1)
#     else:
#         print("Liczba jest pierwsza")
#         return
#
# c = int(input("Podaj liczbe: "))
# prime(c)


#--------------------------------------------------------
#Zaimplementować funkcję n_sums(n: int) -> list[int], która zwróci wszystkie n-cyfrowe liczby
#o takich samych sumach na indeksach parzystych i nieparzystych.

# def n_sums(n: int) -> list[int]:
#     pass

#--------------------------------------------------------
#Zaimplementować funkcję combinations(n: int) -> list[list[int]], która zwróci wszystkie kombinacje w następujący sposób:
# każda z wartości w zakresie od 1 do n wystąpi dokładnie dwa razy, a odległość między tymi elementami będzie równa ich wartości.
# def combinations(n: int) -> list[list[int]]:
#     pass


#--------------------------------------------------------
#Zaimplementować funkcję remove_duplicates(txt: str) -> str,
# # która zwróci wartość parametru txt pozbawioną sąsiadujących duplikujących się znaków.
# def remove_duplicates(txt: str) -> str:
#     for i in range(len(txt)):
#         if i == len(txt) - 1:
#             return txt
#         if txt[i] == txt[i + 1]:
#             return remove_duplicates(txt[:i] + txt[i + 1:])
#
#
#
# str = "XXYZZZ"
# print(remove_duplicates(str))

#--------------------------------------------------------
#Zaimplementować funkcję balanced_parentheses(n: int) -> str,
# która zwróci ciąg znaków o długości n zawierający wszystkie możliwe kombinacje ułożenia nawiasów.
# def balanced_parentheses(n: int) -> str:
#     def pokaz(lewo,prawo,a):
#         if prawo == n:
#             print(a)
#             return
#         if lewo < n:
#             pokaz(lewo + 1, prawo, a + "(")
#         if prawo <lewo:
#             pokaz(lewo, prawo + 1,a + ")")
#
#     pokaz(0, 0, "")
#
# balanced_parentheses(3)

