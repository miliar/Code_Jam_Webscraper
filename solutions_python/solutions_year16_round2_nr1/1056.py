d = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

def number(s):
    n0 = s.count('Z') 
    s = deldig(0,s,n0)
    n6 = s.count('X')
    s = deldig(6,s,n6)
    n2 = s.count('W')
    s = deldig(2,s,n2)
    n7 = s.count('S')
    s = deldig(7,s,n7)
    n4 = s.count('U')
    s = deldig(4,s,n4)
    n1 = s.count('O')
    s = deldig(1,s,n1)
    n5 = s.count('V')
    s = deldig(5,s,n5)
    n9 = s.count('N')/2
    s = deldig(9,s,n9)
    n8 = s.count('G')
    s = deldig(8,s,n8)
    n3 = s.count('H')
    s = deldig(3,s,n3)
    return '0'*n0+'1'*n1+'2'*n2+'3'*n3+'4'*n4+'5'*n5+'6'*n6+'7'*n7+'8'*n8+'9'*n9+'\n'
def deldig(dig, s, num):
    k = s
    for i in range(num):
        for D in d[dig]:
            k.remove(D)
    return k    
    
f = open('input.txt', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    tcs.append(list(f.readline()))

f.close()
f = open('output.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s" % (i+1, number(tcs[i])))
f.close()


