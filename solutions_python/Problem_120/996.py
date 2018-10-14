import math

result = []
f = open('A-small-attempt4.in', 'r')
ans = open('ans.txt', 'w')
T = int(f.readline())

for i in range(1, T+1):
    content = f.readline()
    r, t = list(map(float, content.strip().split()))
    a = 2
    b = (2 * r - 1)
    c = -1 * t
    x = (-1 * b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
        
    if x <= 1:
        x = 1
    else:
        flor = math.floor(x)
        confirmed = 2 * flor**2 + (r*2-1) * flor - t
        if confirmed > 0:
            x = x - 1        
    x = math.floor(x)
    if x == 0:
        x = 1
    ans.write('Case #{0}: {1}\n'.format(i, x))
    
f.close()
ans.close()
