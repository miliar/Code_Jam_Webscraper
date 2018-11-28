# Voorbeeld met for-lussen
kleuren = ["rood", "geel", "blauw", "zwart", "oranje", "paars", "groen"]
hoeveelheid = 0 # Deze variabele wordt gemanipuleerd in de for-lus, dus moet hij hier vooraf worden gedeclareerd

for aantal in kleuren:
    hoeveelheid += 1

print("In mijn doos met kleurpotloden zitten " + str(hoeveelheid) + " potloden.")
# Integers kunnen niet worden geconcateneerd met strings, vandaar de str-functie
# Zie ook http://nl.wikipedia.org/wiki/Concatenatie

>> In mijn doos met kleurpotloden zitten 7 potloden.

# Nog een voorbeeld met for-lussen
kleuren = ["rood", "geel", "blauw", "zwart", "oranje", "paars", "groen"]

print("Mijn doos met kleurpotloden bevat een", end=" ")

for kleur in kleuren:
    if kleur == kleuren[-1]: # Vergelijking met laatste element uit lijst
        print(kleur + " potlood.")
    elif kleur == kleuren[-2]: # Vergelijking met een-na-laatste element uit lijst
        print(kleur, end=" en ")
    else:
        print(kleur, end=", ")

>> Mijn doos met kleurpotloden bevat een rood, geel, blauw, zwart, oranje, paars en groen potlood.
