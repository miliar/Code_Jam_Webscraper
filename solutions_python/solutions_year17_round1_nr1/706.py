fout = open('a-large.out', 'w')

def lp(s, n):
    return (n-len(s))*'0'+s

def doprint(s):
    print(s)
    fout.write(s+'\n')

def close():
    fout.close()

T = int(input())
for tc in range(1, T+1):
    R, C = list(map(int, input().split()))

    v = []
    for i in range(R):
        l = [e for e in input().strip()]
        v.append(l)

    #print(v)

    '''
    Address as: v[y][x]
    R = number of rows, sim. y, i
    C = number of cols, sim. x, j
    '''

    # find what needs to be moved

    ocells = []
    for i in range(R):
        for j in range(C):
            if v[i][j] !=  '?':
                ocells.append([i,j])
    
    #print(ocells)
    # solve

    for cell in ocells:
        y,x = cell

        # top-left coords
        y1 = y
        x1 = x

        # go up
        while y1 >= 1 and x1 >= 0 and v[y1-1][x1] == '?': # y1 overshoots to be less by 1, so..
            y1 -= 1
        #y1 += 1 # .. fix it

        # go left
        while x1 >= 1 and all(l[x1-1] == '?' for l in v[y1 : y+1]): # x1 overshoots to be less by 1, so..
            x1 -= 1
        #x1 += 1
        
        # concomitantly, bottom-right coords
        y2 = y
        x2 = x


        # go right
        while x2 < len(v[y2])-1 and all(l[x2+1] == '?' for l in v[y1 : y2+1]):
            x2 += 1
        #x2 -= 1

            
        # go down
        while y2 < len(v)-1 and all(e=='?' for e in v[y2+1][x1 : x2+1]):
            y2 += 1
            #print('y2',y2)
        #y2 -= 1

        

        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                v[i][j] = v[y][x]
    
        
    doprint("Case #"+str(tc)+":")
    for i in range(len(v)):
        doprint(''.join(v[i]))

close()

'''
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
'''
