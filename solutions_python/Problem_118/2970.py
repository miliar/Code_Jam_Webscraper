# -*- coding: cp1252 -*-
import math
#print int(math.sqrt(9))

# funktion die palindrome findet und zuvor führende nullen entfernt
def ispalindrome(word):
    word = str(word)
    word = word.lstrip("0")
    return word == word[::-1]

# findet heraus ob eine zahl eine perfeke wurzel ist
def is_square(apositiveint):
    #apositiveint = str(apositiveint)
    if apositiveint == 1:
        return True
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def findMatches(min, max):
    count = 0
    for i in range(int(min), int(max)+1):
        if ispalindrome(i):
            if is_square(i):
                # jetzt muss auch noch die wurzel ein palindrom sein
                if ispalindrome(int(math.sqrt(i))):
                    count = count + 1
    return str(count);

#print findMatches("100","1000")
#print is_square(1)
#print ispalindrome("0121")

file = open("C-small-attempt0.in")
ausgabe = open("output2.txt", "w")

erste = True;
i = 1;
for line in file.readlines(): # file würde auch gehen notfalls
    if erste:
        erste = False
        continue
    einzeln = line.split( );
    wiedergabe = "Case #"+str(i)+": " + findMatches(einzeln[0],einzeln[1])
    if i == 1:
        ausgabe.write(wiedergabe)
    else:
        ausgabe.write("\n"+wiedergabe)    
    i=i+1
    print wiedergabe # komma sorgt dafür keine neue zeile zu bekommen

file.close()
ausgabe.close();

