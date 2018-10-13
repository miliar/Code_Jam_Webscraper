#incoming=open('A.txt')
incoming=open('A-large.in')
output=open('A-large.txt','w')
T=int(incoming.readline())
for i in range(1,T+1):
    s=incoming.readline().split()
    R=int(s[0])
    C=int(s[1])
    store={}
    for k in range(R):
        store[k]=[]
        t= incoming.readline().rstrip()
        for element in t:
           store[k].append(element)
    impossible = 0
    for k in range(R):
       for j in range(C):
           if store[k][j] == '#':
               if j == C-1 or k == R-1:
                   impossible = 1
                   break
               elif store[k][j+1] != '#' or store[k+1][j+1] != '#' or store[k+1][j] != '#':
                   impossible = 1
                   break
               else:
                   store[k][j] = store[k+1][j+1] = '/'
                   store[k+1][j] = store[k][j+1] = '\\'
       if impossible == 1:
            break
    if impossible == 1:
        output.write("Case #%d: \nImpossible\n"%i)
    else:
        output.write("Case #%d: \n"%i)
        for row in range(R):
            for column in range(C):
                output.write(store[row][column])
            output.write("\n")

    
incoming.close()
output.close()
