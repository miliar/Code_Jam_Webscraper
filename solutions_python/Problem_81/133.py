#!/usr/bin/python

def parse(M):
    wp = []
    n = []
    for i in M:
        neigh = []
        win = 0.0
        loss = 0.0
        for j in range(len(M)):
            if i[j] == '1':
                win += 1
                neigh.append(j)
            elif i[j] == '0':
                loss += 1
                neigh.append(j)
        wp.append(win/(win + loss))
        n.append(neigh)
    return n,wp

def oop(N):
    nn = [] 
    for i in range(len(N)):
        s = set([])
        for n in N[i]: 
            s.update(N[n])
        nn.append(s)
    return nn

def owp(i,n,M):
    wp = []
    for opp in n[i]:
        win = 0.0
        loss = 0.0
        for j in range(len(M)):
            if M[opp][j] != '.' and j != i:
                if M[opp][j] == '1':
                    win += 1
                else:
                    loss += 1
        wp.append(win / (win + loss))
    return sum(wp)/len(wp) 

def solve(M):
    n,wp = parse(M)
    owps = [owp(i,n,M) for i in range(len(M))]
    oowps = [sum([owps[i] for i in n[j]])/len(n[j]) for j in range(len(M))]
    sol = []
    for i in range(len(M)):
        sol.append(0.25 * wp[i] + 0.5 * owps[i] + 0.25 * oowps[i]) 
    return sol 

r = input()
for c in range(1,r+1):
    t = input()
    M = []
    for i in range(t):
        M.append(raw_input()) 
    sol = solve(M)
    print "Case #%s:" % c
    for i in sol:
        print i
