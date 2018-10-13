import math
def check(sq):
    l = len(sq)
    for i in range (0, l//2):
        if sq[i] != sq[l-i-1]:
            return False
    return True
file = open('C-small-attempt0.in')
outwrite = open('R3.txt', mode = 'w')
n = int(file.readline())
for m in range(1, n+1):
    size = file.readline().split(' ')
    f = int(size[0])
    l = int(size[1])
    s = 0
    for i in range(int(math.sqrt(f - 1)+1), int(math.sqrt(l))+1):
        if check(str(i)) and check(str(i ** 2)):
            s += 1
    outwrite.write('Case #' + str(m)+ ': ' + str(s) + '\n')

file.close()
outwrite.close()
