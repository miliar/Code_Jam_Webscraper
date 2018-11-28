fin = open('A-large.in','r')
fout = open('anspassw.txt', 'w')


T = int(fin.readline())
for i in range(T):
    A, B = map(int, fin.readline().split())
    p = map(float,fin.readline().split())
    third = B+2
    P = 1
    allVars = [third]
    for j in range(A):
        backspace = A - j 
        keystrokes = P*(backspace + B - j + 1) + (1-P) * (backspace + B-j + 1 + B + 1)
        allVars.append(keystrokes)
        P *= p[j]
    allVars.append(P*(B-A + 1) + (1-P)*(B-A + 1 + B + 1))
    ans = min(allVars)
    print i, ans
    fout.write('Case #' + str(i+1) + ': ' + "%.6f" % ans + '\n')

fin.close()
fout.close()
        
        
        
