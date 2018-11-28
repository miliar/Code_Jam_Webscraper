"""
Kaydhi, Google code Jam 2017
Problem A
"""
def pancake_flip(s,k):
    flips=0
    len_s_i=len(s)
    while len(s)>=1 and s[0]:
        s.pop(0)
        
    while len(s)>=k and flips<(len_s_i-k)+2 :
        #print(s)
        for l in range(k):
            s[l]=1-s[l]
        flips+=1
        while len(s)>=1 and s[0]:
            s.pop(0)
    #print(len(s)>=k,flips!=(len(s)-k)+2)
    if len(s)==0:
        return flips
    else:
        return 'IMPOSSIBLE'
    



if __name__=='__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        n=n.replace('+','1').replace('-','0')
        n=[int(j) for j in n]
        m=int(m)
        result=pancake_flip(n,m)
        print("Case #{}: {}".format(i, result))
        
        
