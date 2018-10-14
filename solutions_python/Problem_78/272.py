fname = "A-small-attempt1"
fin = open(fname + '.in', 'r')
fout = open(fname + '.out', 'w')

T = int(fin.readline())
for i in range(T):
    line = fin.readline().split(' ')
    N = int(line[0])
    P_d = int(line[1])
    P_g = int(line[2])

    answer = "Broken"
    D = 0

    for D in range(1,N+1):
        if D * P_d % 100 == 0:
            won = D * P_d
            total = D

            if P_g == 100 and P_d != P_g:
                answer = "Broken"
            elif P_g == 0 and P_d != P_g:
                answer = "Broken"
            else:
                answer = "Possible"
            
            
            
          
        
    fout.write('Case #{0}: {1}\n'.format(i+1, answer))

fin.close()
fout.close()
    
