from sys import stdin
read = stdin.readline

ints = lambda:map(int,read().split())
doubles = lambda:map(float,read().split())

def split(s1,s2,p1,p2):
    if len(s1) == p1 and len(s2) == p2: return 0
    if s1[p1] == s2[p2]: return split(s1,s2,p1+1,p2+1)
    res1 = 1000000
    res2 = 1000000
    res3 = 1000000
    res4 = 1000000
    # Ta bort fran s1 
    if p1 > 0 and p2 > 0 and s1[p1] == s1[p1-1]:
        res1 = 1 + split(s1,s2,p1,p2-1)
    # Ta bort fran s2
    if p2 > 0 and p1 > 0 and s2[p2] == s2[p2-1]:
        res2 = 1 + split(s1,s2,p1-1,p2)
    # Lagg till pa s1
    """
    if p1 > 0 and (p1 >= len(s1) or s1[p1] == s1[p1-1]):
        res3 = 1 + split(s1,s2,p1,p2)
    # Lagg till pa s2
    if p2 > 0 and s2[p2] == s2[p2-1]:
        res4 = 1 + split(s1,s2,p1,p2-1)
    """
    return min(res1,res2,res3,res4)

def solve():
    N = ints()[0]
    s1 = read()
    s2 = read()
    splits = split(s1,s2,0,0)
    if splits >= 1000000: return "Fegla Won"
    return str(splits)




for t in range(ints()[0]):
  ans = solve()
  print "Case #%d: %s" % (t+1,ans)