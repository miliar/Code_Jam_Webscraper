T = int(input())
originals = []

for i in range(T):
    originals.append(input())

d1 = "abcdefghijklmnopqrstuvwxyz"
d2 = "yhesocvxduiglbkrztnwjpfmaq"

for i in range(T):
    translated = originals[i].translate(str.maketrans(d1, d2))
    print("Case #" + str(i+1) + ": " + translated)