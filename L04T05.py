etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")
etunimiLen = len(etunimi)
etunimiLenLista = list(etunimi)
print(etunimiLenLista[0]*etunimiLen)
sukunimiLen = len(sukunimi)
tulos =""
sukunimiLen = sukunimiLen - 1
while sukunimiLen>-1:
    tulos += sukunimi[sukunimiLen]
    sukunimiLen = sukunimiLen - 1
  
print(tulos)

