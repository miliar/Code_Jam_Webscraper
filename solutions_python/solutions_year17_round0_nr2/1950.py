# Google Code Jam 2016
# Qualification Round
# Problem B. Tidy Numbers

import sys

def is_tidy(n):
    lst = list( str(n) )
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))


def tidy_numbers_naive(n):
    for i in xrange(n,0,-1):
        if is_tidy(i):
            return i
    return None


def tidy_numbers(n):
    if is_tidy(n):
        return n
    
    digits = list( str(n) )
    
    # m: the tidy number
    m = []
    m.append(digits[-1])
    
    for i in range(len(digits)-1,0,-1):
        # m = ... d1 d0
        d0 = int(m[0])
        d1 = int(digits[i-1])
        
        if d1 <= d0:
            m.insert(0, str(d1))
        else:
            m[0] = '9'
            m.insert(0, str(d1-1))
            
            if is_tidy( int("".join(m)) ) == False:
                for j in range(2, len(m)):
                    m[j] = '9'
            
    for i in range(len(m)):
        if m[i] == '0':
            m.pop(0)
        else:
            break
    
    return "".join(m)


def solver():
    # t: the number of cases
    t = int(raw_input())
    
    for i in xrange(1, t+1):
        line = raw_input().split(' ')

        n = int(line[0])

        ans = tidy_numbers(n)
        
        print "Case #{}: {}".format(i, ans)


def main():
    solver()

if __name__ == '__main__':
    main()