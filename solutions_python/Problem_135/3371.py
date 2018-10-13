


def analyze(case, f, pass1, pass2):
    set1 = pass1[1][pass1[0]-1]
    set2 = pass2[1][pass2[0]-1]
    common = 0
    card = 0
    for i in set1:
        if i in set2:
            card = i
            common += 1
    if common == 1:
        f.write("Case #{0}: {1}\n".format(case, card))
    elif common > 1:
        f.write("Case #{0}: Bad magician!\n".format(case))
    else:
        f.write("Case #{0}: Volunteer cheated!\n".format(case))


def getset(l, x):
    answer = int(l[x])
    r = []
    r.append([int(n) for n in l[x+1].split(' ')])
    r.append([int(n) for n in l[x+2].split(' ')])
    r.append([int(n) for n in l[x+3].split(' ')])
    r.append([int(n) for n in l[x+4].split(' ')])
    return answer, r

#f = file("input.txt")
f = file("A-small-attempt0.in")
l = f.readlines()
f.close()

f = file("output.txt", "w")

count = int(l[0])
n = 0
while n < count:
    analyze(n+1, f, getset(l, n*10 + 1),getset(l, n*10 + 6))
    n += 1

f.close()
