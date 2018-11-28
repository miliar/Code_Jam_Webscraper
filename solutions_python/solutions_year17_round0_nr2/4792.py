def tidy_numbers(n):
    sol = n
    for i in range(n,0,-1):
        if td(i):
            return i

def td(n):
    sol = True
    aux = 0
    for i in range(0,len(str(n))):
        if int(str(n)[i])<aux:
            return False
        else:
            aux = int(str(n)[i])
    return sol

if __name__ == '__main__':
    a = int(raw_input())
    cases = []
    for i in range(a):
        cases.append(int(raw_input()))
    k = 1
    for i in cases:
        print "Case #{}: {}".format(k,tidy_numbers(i))
        k += 1
