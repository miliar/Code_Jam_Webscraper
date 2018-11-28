def rm(letters,z):
    for l in letters:
        z[l] = z[l] - 1
        if z[l] < 0:
            print "error"
        if z[l] == 0:
            del z[l]

def has_num(n,z):
    if n == 0 and 'Z' in z:
        rm(['Z','E','R','O'],z)
        return True
    if n == 1 and 'O' in z and 'N' in z and 'E' in z:
        rm(['O','N','E'],z)
        return True
    if n == 2 and 'W' in z:
        rm(['T','W','O'],z)
        return True
    if n == 3 and 'T' in z and 'H' in z and 'R' in z and 'E' in z and z['E'] >= 2:
        rm(['T','H','R','E','E'],z)
        return True
    if n == 4 and 'U' in z:
        rm(['F','O','U','R'],z)
        return True
    if n == 5 and 'F' in z:#f
        rm(['F','I','V','E'],z)
        return True
    if n == 6 and 'X' in z:#x
        rm(['S','I','X'],z)
        return True
    if n == 7 and 'S' in z and 'E' in z and 'V' in z and 'E' in z and 'N':#v
        rm(['S','E','V','E','N'],z)
        return True
    if n == 8 and 'G' in z:#g
        rm(['H','E','I','G','T'],z)
        return True
    if n == 9 and 'N' in z and 'I' in z and 'N' in z and 'E' in z:#i
        rm(['N','I','N','E'],z)
        return True

def solveone(inputstr):
    z = dict()
    for i in range(len(inputstr)):
        letter = inputstr[i]
        if letter in z:
            z[letter] = z[letter]+1
        else:
            z[letter] = 1

    num = ""
    curr = 0
    for i in xrange(0,10,2):
        curr = i
        next = False
        while not next:
            if has_num(curr, z):
                num += ""+str(curr)
            else:
                next = True

    for i in xrange(1,11,2):
        curr = i
        next = False
        while not next:
            if has_num(curr, z):
                num += ""+str(curr)
            else:
                next = True
    return num

i = 0
with open('in.txt') as f:
    for line in f:
        if i != 0:
            line = line.strip()
            n = solveone(line)
            print "Case #"+str(i)+": "+''.join(sorted(n))
        i += 1

"""
ZERO => Z
TWO => W
FOUR => U
SIX => X
EIGHT => G

ONE => O
THREE => H
FIVE => F
SEVEN => S
NINE => I
    """