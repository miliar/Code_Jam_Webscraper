f= open("A-small-attempt3.in")
T =f.readline()

T= int(T)
G= []
S= []
for i in range(0,T):
    G.append(f.readlines())
f.close()
G=G[0]

for i in range(0,T):
    S.append('')
    for j in range(0,len(G[i])):
        if G[i][j] == 'y':
            S[i]+=('a')
            
        elif G[i][j] == 'n':
            S[i]+=('b')
            
        elif G[i][j] == 'f':
            S[i]+=('c')
            
        elif G[i][j] == 'i':
            S[i]+=('d')
            
        elif G[i][j] == 'c':
            S[i]+=('e')
            
        elif G[i][j] == 'w':
            S[i]+=('f')
            
        elif G[i][j] == 'l':
            S[i]+=('g')
            
        elif G[i][j] == 'b':
            S[i]+=('h')
            
        elif G[i][j] == 'k':
            S[i]+=('i')
            
        elif G[i][j] == 'u':
            S[i]+=('j')
            
        elif G[i][j] == 'o':
            S[i]+=('k')
            
        elif G[i][j] == 'm':
            S[i]+=('l')
            
        elif G[i][j] == 'x':
            S[i]+=('m')
            
        elif G[i][j] == 's':
            S[i]+=('n')
            
        elif G[i][j] == 'e':
            S[i]+=('o')
            
        elif G[i][j] == 'v':
            S[i]+=('p')
            
        elif G[i][j] == 'z':
            S[i]+=('q')
            
        elif G[i][j] == 'p':
            S[i]+=('r')
            
        elif G[i][j] == 'd':
            S[i]+=('s')
            
        elif G[i][j] == 'r':
            S[i]+=('t')
            
        elif G[i][j] == 'j':
            S[i]+=('u')
            
        elif G[i][j] == 'g':
            S[i]+=('v')
            
        elif G[i][j] == 't':
            S[i]+=('w')
            
        elif G[i][j] == 'h':
            S[i]+=('x')
            
        elif G[i][j] == 'a':
            S[i]+=('y')
            
        elif G[i][j] == 'q':
            S[i]+=('z')
            
        elif G[i][j] == ' ':
            S[i]+=(' ')
        elif G[i][j] == '\n':
            S[i]+=('')

f = open('output.txt', 'w')

for i in range(0,T):
    f.write('Case #'+str(i+1)+': '+S[i]+'\n')
f.close()


    
