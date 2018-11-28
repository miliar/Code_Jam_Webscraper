import gmpy2

T = int(raw_input()) + 1

for i in range(1, T):
    
    line = raw_input()
    [A, B] = line.split(' ')
    A = int(A)
    B = int(B)
    fairsquare = 0
    
    for x in range(A, B + 1):
        if gmpy2.is_square(x) and str(x) == str(x)[::-1]:
            root = int(gmpy2.sqrt(x))
            if str(root) == str(root)[::-1]:
                fairsquare = fairsquare + 1

    print 'Case #' + str(i) + ': ' + str(fairsquare)
