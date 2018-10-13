from sys import stdin

def read_ints():
    return map(int, stdin.readline().rstrip().split(' '))

def mirror(s, double):
    return int(s + s[::-1] if double else s[:-1] + s[::-1])
    
def next_palindrome(n):
    s = str(n)
    lens = len(s)
    half = s[:(lens - 1) / 2 + 1]
    double = True if lens % 2 == 0 else False
    np = mirror(half, double)
    if np <= n:
        lenhalf = len(half)
        np = str(int(half) + 1)
        if lenhalf == len(np):
            np = mirror(np, double)
        else:
            if not double:
                np = np[:-1]
            np = mirror(np, not double)
    return np
        
def is_palin(n):
    s = str(n)
    return s == s[::-1]
    
def find(n, fas):
    for i in xrange(len(fas)):
        if fas[i] >= n:
            return i
    return len(fas)
    
def gen_fas(max):
    fas = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944]
    bases = []
    fasappend = fas.append
    candidates = [['00', '11'], ['000', '010', '020', '101', '111', '121', '202', '212']]
    square, current = 121, 0
    while square < max:
        lc = len(candidates[current])
        #print square, len(str(square)), lc, len(fas)
        temp = []
        for d in ('0', '1'):
            for i in xrange(lc):
                c = candidates[current][i]
                if c and c[0] != '2':
                    temp.append(d + c + d)
        temp.append('2' + candidates[current][0] + '2')
        if current == 1:
            temp.append('2' + candidates[current][1] + '2')
        candidates[current] = temp
        for i in xrange(len(candidates[current])):
            c = candidates[current][i]
            if c[0] != '0':
                n = int(c)
                square = n * n
                if square > max:
                    break
                if is_palin(square):
                    fasappend(square)
                    bases.append(n)
                    #print 'cooool: ', c
                else:
                    #print 'shitty: ', c
                    candidates[current][i] = None
        current = 1 if current == 0 else 0
            
    return fas, bases
    
def main():
    MAX = 10 ** 100
    fas, bases = gen_fas(MAX)
    #print fas[-1]
    #print len(fas)
    
    T = int(stdin.readline())
    for Ti in xrange(T):
        A, B = read_ints()
        answer = find(B + 1, fas) - find(A, fas)
        print 'Case #{}: {}'.format(Ti + 1, answer)

main()
