def get_fuel(km, kskulutus):
    return km*kskulutus/100

print(get_fuel(100,7.5), "ltr")
tokamatka = get_fuel(220,6.9)
x = round(tokamatka, 1)
print(x,"ltr")
