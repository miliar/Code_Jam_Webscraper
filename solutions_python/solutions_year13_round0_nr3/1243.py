import sys

def gen_single():
    #return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return ['0', '1', '2']

def gen_double(mid=''):
    return ['%(g)s%(mid)s%(g)s' % {'g': g, 'mid': mid} \
            for g in gen_single()]


def gen_palindromes(n):
    p_n = []
    p_e = []
    prev_n = 0
    prev_e = 0
    for l in range(1, n+1):
        #print 'Level %s...' % l
        if l == 1:
            p_n.extend(gen_single())
            prev_n = len(p_n)
            continue
        if l == 2:
            d = gen_double()
            p_e.extend(d)
            prev_e = len(d)
            continue
        if l%2 == 1:
            p = p_n
            prev = prev_n
        else:
            p = p_e
            prev = prev_e
        mid = p[-1*prev:]

        new_p = []
        new_p.extend(map(
                lambda x: gen_double(
                    mid=x),
                mid))
        count = 0
        for item in new_p:
            for num in item:
                x = int(num)
                if check_palindrome(x*x):
                    count += 1
                    p.append(num)
        prev = count
        if l%2 == 1:
            prev_n = prev
        else:
            prev_e = prev

    #p = p_n + p_e
    p = p_n + p_e + ['3']
    return sorted([int(P)**2 for P in p if P[0] != '0'])

def check_palindrome(x):
    s = str(x)
    l = len(s)
    for i in range(l):
        if s[i] != s[l-i-1]:
            return False
    return True

if __name__ == '__main__':
    palindromes = gen_palindromes(52)

    f = open(sys.argv[1])
    T = int(f.readline())
    for t in range(T):
        N, M = [int(i) for i in f.readline().split()]
        count = 0
        for p in palindromes:
            if p > M:
                break
            if p >= N:
                count += 1
        print 'Case #%s: %s' % (t+1, count)

