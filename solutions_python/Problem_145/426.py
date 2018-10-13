'''
Created on 13.04.2013

@author: Alex
'''
from fractions import gcd

def analyse(a, b):           
    count = 1
    while b / a > 2 and a > 1:
        count += 1
        b = int(b / 2)
        a -= 1
        gc = gcd(a,b)
        b = int(b / gc)
        a = int(a / gc)
    if a == 1 and b / a > 2:
        while b > 2:
            count += 1
            b = int(b / 2)
    if count > 40:
        return 'impossible'
    return str(count)
     
def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

if __name__ == '__main__':
    f = open('in/A-large.in', mode='r')
    g = open('out/A-large.out', mode='w')
    n = int(f.readline())
    for i in range(1,n+1):
        line = f.readline()
        a = int(line.split('/')[0])
        b = int(line.split('/')[1]) 
        gc = gcd(a,b)
        a = int(a/gc)
        b = int(b/gc)
        if not is_power2(b):
            g.write('Case #' + str(i) + ': impossible\n')
        elif b/a < 2:
            g.write('Case #' + str(i) + ': 1\n')          
        else:
            g.write('Case #' + str(i) + ': ' + analyse(a, b) + '\n')