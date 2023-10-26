def get_cost(km, kskulutus, lhinta):
    return km*kskulutus/100*lhinta

ekaHinta = (get_cost(100,7.5,1.88))
tokaHinta = (get_cost(220,6.9,1.88))
x = round(ekaHinta, 2)
y = round(tokaHinta, 2)
print(x,"€")
print(y,"€")
