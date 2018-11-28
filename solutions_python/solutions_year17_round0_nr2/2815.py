import sys

cases = []

with open(sys.argv[1]) as f:
    for i in range(1,int(f.readline())+1):        
        n = list(f.readline())[:-1]
        untidy = False
        allSame = True

        for j in range(1,len(n)):
            if allSame and n[j-1] != n[0]:
                allSame = False            
            
            if not untidy and int(n[j]) < int(n[j-1]):                
                untidy = True
                if allSame:
                    n[0] = str(int(n[j-1])-1)
                    for k in range(1,j):
                        n[k] = '9'
                else:
                    n[j-1] = str(int(n[j-1])-1)
            
            if untidy: n[j] = '9'
            
        if n[0] == '0': n = n[1:]
        s = 'Case #'+str(i)+': '+''.join(n)+'\n'
        print(s)
        cases.append(s)

with open(sys.argv[2],'w+') as g:
    g.writelines(cases)
#             