'''
Created on 2010/05/23

@author: banana
'''

if __name__ == '__main__':
    pass


dic = {}
ans = {}



fact = [1 for x in range(501)]

for i in range(1, 501):
    fact[i] = i * fact[i-1]

def combi(n, r):
    return fact[n] / (fact[r] * fact[n-r])

def solve(n, pos):
    #fpout.write("%d, %d\n"%(n, pos))
   
    if pos == 1:
        return 1
    elif pos <= 0:
        return 0
    
    if dic.has_key((n, pos)):
        return dic[(n, pos)]
    
    c = 0
    dist = n-pos
    for i in range(1, dist+1):
        c = c + solve(pos, pos-i) * combi(dist-1, i-1)
    
    dic[(n,pos)] = c % 100003
    return c



def calc_ans(n):
    c = 0
    for i in range(1, n):
        c = c + solve(n, i)
        
    ans[n] = c % 100003
    print n,ans[n]
    
calc_ans(500)
    
fp = open("C-large.in", "r")
fpout = open("2C-large.txt", "w")
line = fp.readline()

T = int(line)

for t in range(1, T+1):
    n = int(fp.readline().split()[0])
    if not ans.has_key(n):
        calc_ans(n)
    fpout.write("Case #%d: %d\n" % (t, ans[n]))
    

    
    
    