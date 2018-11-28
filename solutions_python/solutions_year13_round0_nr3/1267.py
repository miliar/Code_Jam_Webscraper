import math
import re
def is_pal(num):
    l = len(num)
    if l == 1:
        return True
    elif l % 2 == 0:
        for i in range(int(l/2)):
            if num[i] != num[l-1-i]:
                return False
        return True
    else:
        return is_pal(num[:math.floor(l/2)] + num[math.ceil(l/2):])
    
def solve_range(x,y):
    a = math.ceil(pow(x,1/2))
    b = math.floor(pow(y,1/2))

    count = 0
    for i in range(a,b+1):
        if is_pal(str(i)):
            if is_pal(str(i*i)):
                count +=1
    return count

def find_fair(filename, output):
    f = open(filename, 'r')
    p = re.compile(r'([0-9]+)')
    cases = int(p.match(f.readline()).group())
    results = []
    for i in range(cases):
        r = p.findall(f.readline())
        results.append(solve_range(int(r[0]),int(r[1])))
        
    f.close()
    f = open(output, 'w')
    for i in range(cases):
        f.write('Case #{}: '.format(i+1) +str(results[i]) +'\n')
    f.close
