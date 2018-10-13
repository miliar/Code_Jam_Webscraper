import math
def revint(i):
    ni = str(i)[::-1]
    ni = int(ni)
    return ni
def ReadInput(f):
    text = f.read()
    bounds = text.split()
    cases = int(bounds[0])
    for i in range(0,(cases)):
        lb = int(bounds[2*i+1])
        ub = int(bounds[2*i+2])
        nlb = int(math.ceil(lb**.5))
        nub = int(math.floor(ub**.5))
        cand = []
        ans = []
        for n in range(nlb, nub+1):
            if n == revint(n):
                cand.append(n)
        for e in cand:
            if e**2 == revint(e**2):
                ans.append(e)
        print 'Case #'+str(i+1)+': '+str(len(ans))

f = file('Csmall1.txt')
ReadInput(f)



            
    
