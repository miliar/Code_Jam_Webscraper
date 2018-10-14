from math import log10

def Tidy(n):
    #print("n = {}".format(n))
    if len(n) <= 1:
        return n
    sub = Tidy(n[1:])
    if int(n[0]) <= int(sub[0]):
        #print("now n = {}".format(n[0] + sub))
        return n[0] + sub
    n = ''.join([str(int(n[0]) - 1)] + ['9' for char in sub])
    #print("now n = {}".format(n))
    return n

cases = int(input())
for i in range(cases):
    print("Case #{}: {}".format(i + 1, int(Tidy(input()))))

'''
def SlowTidy(n):
    while 1:
        for i in range(len(n) - 1):
            if int(n[i]) > int(n[i + 1]):
                break
        else:
            break
        n = str(int(n) - 1)
    return n

for i in range(500, 1000):
    print("SlowTidy({}) = {}, Tidy({}) = {}".format(i, SlowTidy(str(i)), i, Tidy(str(i))))
    if int(SlowTidy(str(i))) != int(Tidy(str(i))):
        print("Difference")
'''
