f = open('A-small-attempt8.in','r')
T = f.readline()
T = int(T[0:-1])
for TC in range(0,T):
    P = f.readline()
    [string, N] = P.split()
    N = int(N)
    vowels = ['a','e','i','o','u']

#    string = 'tsetse'
#    N = 2
    d = []
    for p in range(N):
        d.append(1)
            
    v = []
    for n in string:
        if n in vowels:
            v.append(0)
        else:
            v.append(1)
    
    length = len(v)
    count = 0

            
    if N > -1:
        for start in range(0,length):
            for end in range(start, length):
            
#        print(str(start) + ' ' + str(end))
#        print(v[start:end+1])
                p = v[start:end+1]
#print(p)
                if N == 1 and 1 in p:
                    count += 1
                elif N > 1:
#            print(str(start) +' ' + str(end) + ' ' + str(p))
                    plength = len(p)
                    if plength >= N:
                        pt = 0
                        bk = 0
                        for start2 in range(0,plength - 1):
                            if N > 1 and p[start2:start2+N] == d:
                                count += 1
                                break

    print("Case #" +str(TC+1) + ": " + str(count))

