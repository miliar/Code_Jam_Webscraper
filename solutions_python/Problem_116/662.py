def check(A):
    g = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]
    d = []
    Xcount = 0
    Ocount = 0
    for x in A:
        for y in x:
          if y == '.':
              d.append(0)
          elif y == 'X':
              d.append(1)
              Xcount += 1
          elif y == 'O':
              d.append(2)
              Ocount += 1
          else:
              d.append(3)
#    print(d)
    p1win = 0
    p2win = 0
    for c in g:
        e = set()
        for f in c:
            e.add(d[f])
#        print(e)
        if e == set([1,3]) or e == set([1]):
            p1win = 1
        if e == set([2,3]) or e == set([2]):
            p2win = 1
#    print(p1win)
#    print(p2win)
    if p1win == 0 and p2win == 0:
        if 0 in d:
            print('Case #' + str(TC+1) + ': Game has not completed')
        else:
            print('Case #' + str(TC+1) + ': Draw')
    elif p1win == 1 and p2win == 0:
        print('Case #' + str(TC+1) + ': X won')
    elif p1win == 0 and p2win == 1:
        print('Case #' + str(TC+1) + ': O won')
    elif p1win == 1 and p2win == 1:
        if Xcount == Ocount:
            print('Case #' + str(TC+1) + ': X won')
        elif Xcount > Ocount:
            print('Case #' + str(TC+1) + ': O won')
        else:
            print('Case #' + str(TC+1) + ': O won')
                

def test():
    A = ['OOXX','OXXX','OX.T','O..O']
    check(A)
    
global TC
f = open('A-large.in','r')
T = f.readline()
T = int(T[0:-1])
for TC in range(0,T):
    AA = []
    for w in range(0,4):
        CC = f.readline()
        CC = CC[0:4]
        AA.append(CC)
    dummy = f.readline()
    check(AA)    
        
