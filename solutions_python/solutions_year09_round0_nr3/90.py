'''
Created on 3 Sep 2009

@author: Maksims Rebrovs
'''
data = open("c.in")
N = int(data.readline())
target = "welcome to code jam"
#         0123456789abcdefghi
def positions(c):
    if c == 'w' : return (0,)
    elif c == 'e' : return (1,6,14)
    elif c == 'l' : return (2,)
    elif c == 'c' : return (3, 11)
    elif c == 'o' : return (4,9,12)
    elif c == 'm' : return (5,18)
    elif c == ' ' : return (7,10,15)
    elif c == 't' : return (8,)
    elif c == 'd' : return (13,)
    elif c == 'j' : return (16,)
    elif c == 'a' : return (17,)
    else: return ()

line = "welcome to codejam"


def jamcount(s):
    term = [[0 for i in range(19)] for j in range(len(s))]
    n = 0
    while n < len(s):
        c = s[n]
        for p in positions(c):
            if p == 0:
                term[n][0] = 1
                continue
            psum = 0
            for i in range(n):
                psum = (psum + term[i][p-1]) % 10000
            term[n][p] = psum
        n +=1
    #for i in range(len(term)): 
   #     print line[i], term[i]
    return sum(term[i][18] for i in range(len(term))) % 10000
        


for i in range(N):
    print "Case #%d: %04d" % (i+1, jamcount(data.readline()))
    