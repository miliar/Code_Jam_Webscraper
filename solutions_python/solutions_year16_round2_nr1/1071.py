__author__ = 'Owen'

def GettingDigits(S):
    phone = ""
    card = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = {}

    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters[i] = 0;

    for i in S:
        for j in i:
            letters[j] += 1


    card[0] = letters["Z"]
    letters["E"] -= letters["Z"]
    letters["R"] -= letters["Z"]
    letters["O"] -= letters["Z"]
    letters["Z"] = 0

    card[2] = letters["W"]
    letters["T"] -= letters["W"]
    letters["O"] -= letters["W"]
    letters["W"] = 0

    card[6] = letters["X"]
    letters["S"] -= letters["X"]
    letters["I"] -= letters["X"]

    card[7] = letters["S"]
    letters["E"] -= letters["S"]
    letters["V"] -= letters["S"]
    letters["E"] -= letters["S"]
    letters["N"] -= letters["S"]
    letters["S"] -= letters["S"]

    card[5] = letters["V"]
    letters["F"] -= letters["V"]
    letters["I"] -= letters["V"]
    letters["E"] -= letters["V"]
    letters["V"] -= letters["V"]

    card[4] = letters["F"]
    letters["O"] -= letters["F"]
    letters["U"] -= letters["F"]
    letters["R"] -= letters["F"]
    letters["F"] -= letters["F"]

    card[3] = letters["R"]
    letters["T"] -= letters["R"]
    letters["H"] -= letters["R"]
    letters["E"] -= letters["R"]
    letters["E"] -= letters["R"]
    letters["R"] -= letters["R"]

    card[8] = letters["T"]
    letters["E"] -= letters["T"]
    letters["I"] -= letters["T"]
    letters["G"] -= letters["T"]
    letters["H"] -= letters["T"]
    letters["T"] -= letters["T"]

    card[9] = letters["I"]
    letters["N"] -= letters["I"]
    letters["N"] -= letters["I"]
    letters["E"] -= letters["I"]
    letters["I"] -= letters["I"]

    card[1] = letters["O"]

    for i in range(len(card)):
        for j in range(int(card[i])):
            phone += str(i)

    return phone








f = open("A-large.in", "r")
a = []
for line in f:
    a.append(line)

print a[0]


with open("A-l.txt", "w") as text_file:
    for i in range(int(a[0])):
        s = ""
        for j in range(len(a[i+1])-1):
            s += a[i+1][j]

        text_file.write("Case #%s: %s \n" %(i+1, GettingDigits(s)))





