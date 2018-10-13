'''
Created on 13.09.2009

@author: Vlad Dumitrescu
'''

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def one(x):
    return 1

def compute_bribe(c, m):
    sum = 0
    for i in reversed(c[0:m]):
        if i == 0: break
        sum += 1
    for i in c[m+1:]:
        if i == 0: break
        sum += 1
    return sum

if __name__ == '__main__':
    # open input and output files
    fin = open('C-small.in', 'r')
    fout = open('C-small.out', 'w')
    
    T = int(fin.readline())
    j = 0
    while T > 0:
        j += 1
        fout.write('Case #' + str(j) + ': ')
        [P, Q] = map(int, fin.readline().split())
        iR = all_perms(fin.readline().split())
        min = 4000000000
        for R in iR:
            cells = map(one, range(0,P))
            R = map(int, R)
            b = 0
            for i in R:
                cells[i-1] = 0
                b += compute_bribe(cells, i-1)
            if b < min:
                min = b
        fout.write(str(min))
        fout.write("\n")
        T -= 1
    fin.close()
    fout.close()