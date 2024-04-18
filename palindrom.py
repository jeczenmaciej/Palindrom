def czy_palindrom(wyraz):
    wyraz=wyraz.replace(" ", "").lower()
    return wyraz==wyraz[::-1]
print(czy_palindrom("kajak"))
print(czy_palindrom("Potop"))
print(czy_palindrom("Python"))