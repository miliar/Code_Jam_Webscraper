import string

f = open('D-large.in', 'r')
g = open('output.txt', 'w')

n = int(f.readline())
count = 1

# b1: Naomi, b2: Ken
def solve_nocheat(b1, b2):
    l = len(b1)
    score = 0
    while(l > 0):
        if(b1[-1] > b2[-1]):
            score += 1
            b1 = b1[:-1]
            b2 = b2[1:]
        else:
            i = l - 1
            while i >= 0 and b2[i] > b1[-1]:
                i-=1
            b1 = b1[:-1]
            b2.remove(b2[i+1])
        l = len(b1)
    return score

def solve_cheat(b1, b2):
    l = len(b1)
    score = 0
    while(l > 0):
        if(b1[-1] < b2[-1]):
            b1 = b1[1:]
            b2 = b2[:-1]
        else:
            score += 1
            b1 = b1[:-1]
            b2 = b2[:-1]
        l = len(b1)
    return score

while count <= n:
    f.readline()
    b1 = sorted([float(x) for x in string.split(f.readline()[:-1])])
    b2 = sorted([float(x) for x in string.split(f.readline()[:-1])])
    g.write("Case #%d: %d %d\n" % (count, solve_cheat(b1[:], b2[:]), solve_nocheat(b1[:], b2[:])))
    
    count += 1

f.close()
g.close()