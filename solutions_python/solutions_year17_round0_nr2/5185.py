nb = int(input())
cases = []
for loop in range(nb):
    cases.append(int(input()))

#print(cases)


def gen_min(x):
    s = str(x)
    n = len(s)

    for i in range(n,0,-1):
        for j in range(9,0,-1):
            y =int(str(j)*i)
            if y < x:
                #print("gen", y)
                return y

    return 0

def tidy(n):
    l = list(str(n))

    for i in range(len(l) - 1):
        if int(l[i]) > int(l[i + 1]) :
            return False

    return True


for i in range(nb):

    min = gen_min(cases[i])
    max = min

    for x in range(cases[i], min,-1):
        if tidy(x):
            max = x
            break


    print("Case #"+str(i + 1) +": " + str(max))