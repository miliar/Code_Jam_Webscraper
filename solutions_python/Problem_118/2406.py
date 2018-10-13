import math
def check_palendromes(x):
    return str(x) == str(x)[::-1]
def square_and_pal(x,y):
    score = 0
    while x <= y:
        if not (math.sqrt(x) % 1):
            score += check_palendromes(x)*check_palendromes(int(math.sqrt(x)))
        x = x + 1
    return score
f = open('C-small-attempt0-1.in', 'r')
n = int(f.readline().strip())
output = ''
for i in range(n):
    if i > 0:
        output += '\n'
    L = f.readline().strip().split()
    score = square_and_pal(int(L[0]),int(L[1]))
    output += 'Case #' + str(i + 1) +': '+str(score)
f.close()
f = open('C-small-attempt0-1.out', 'w')
f.write(output)
f.close()