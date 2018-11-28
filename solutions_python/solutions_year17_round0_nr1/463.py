import sys
sys.setrecursionlimit(2000)

def flip(K, p, pos):
    for i in range(pos, pos+K): p = p[:i]+('-' if p[i] == '+' else '+')+p[i+1:] 
    return p
    
def evalAns(K, p):
    # end of recursion
    if '-' not in p or len(p) == 0: return 0
    if len(p) < K: return "IMPOSSIBLE"
    if len(p) == K and ('-' in p and '+' in p): return "IMPOSSIBLE"
    if len(p) == K and '+' not in p: return 1
    
    # recursion
    i = 0
    while i < len(p) and p[i] == '+': i += 1
    if i > 0: return evalAns(K, p[i:])
    
    p = flip(K, p, 0)
    i = 0
    while i < len(p) and p[i] == '+': i += 1
    b = evalAns(K, p[i:])
    if b == "IMPOSSIBLE": return b
    else: return 1 + b

def main():
    # read the input file
    f = open("A-large.in", "r")
    s = f.read().split("\n")
    f.close()
    
    T = eval(s.pop(0))
    outputsStr = ""
    for i in range(T):
        p, K = s.pop(0).split()
        K = eval(K)
        res = evalAns(K, p)
        outputsStr += "Case #%d: %s%s" % (i+1, str(res), "\n" if i < T-1 else "")
    
    f = open("a-large.out", "w")
    f.write(outputsStr)
    f.close()

main()
