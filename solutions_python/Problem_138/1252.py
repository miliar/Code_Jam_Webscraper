
def war(n, p1, p2):
    p1Score, p2Score = 0,0
    p1.sort()
    p2.sort()
    for i in range(n):
        m = p1.pop()
        if p2[-1] < m:
            p2.pop(0)
            p1Score += 1
        else:
            for i in p2:
                if i > m:
                    p2.remove(i)
                    p2Score += 1
                    break
    return p1Score

def D_war(n, p1, p2):
    p1Score, p2Score = 0,0
    p1.sort()
    p2.sort()
    for i in range(n):
        flag = True
        for i in range(len(p1)):
            if p1[i] < p2[i]:
                flag = False
        if flag:
            p1Score = p1Score + len(p1)
            return p1Score
        else:
            p2.pop()
            p1.pop(0)
            p2Score += 1
    return p1Score


file = open('input.txt')

t = int(file.readline())
output = [0]*t

for i in range(t):
    n = int(file.readline())

    temp = file.readline()
    temp = temp.split()
    naomi = [float(x) for x in temp]

    temp = file.readline()
    temp = temp.split()
    ken = [float(x) for x in temp]
    naomi_copy = naomi.copy()
    ken_copy = ken.copy()
    output[i] = "Case #" + str(i+1) + ": " + str(D_war(n, naomi_copy, ken_copy)) + " " + str(war(n, naomi, ken))

file.close()

file = open('output.txt', 'w')

for i, o in enumerate(output):
    file.write(o + "\n")

file.close()

