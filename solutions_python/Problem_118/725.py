fin  = open('C-large-1.in', 'r')
fout = open('C-large.out', 'w')

def ifpalidrome(x):
    s = str(x)
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[-1 * (i + 1)]:
            return False
    return True
    
perfectsq = [x * x for x in range(1, pow(10, 7)) if ifpalidrome(x)
                                  and ifpalidrome(x * x)]

def countFairSq():
    c = 0
    minNum, maxNum = map(int, fin.readline().split())
    for x in perfectsq:
        if x >= minNum and x <= maxNum:
            c = c + 1
    return c
    
if __name__ == '__main__':
    
    count = fin.readline()
    for j in range(int(count)): 
        fout.write('Case #{0}: {1}\n'.format(j + 1, countFairSq()))

    fin.close()
    fout.close()
