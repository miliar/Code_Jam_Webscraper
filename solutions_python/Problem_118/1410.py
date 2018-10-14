import fileinput

f = fileinput.input()
# f = fileinput.input('sample.in')

T = int(f.readline())


def p(x):
    return x==''.join(reversed(x))

def nfs(ab):
    # print(ab)
    la, lb = map(len, ab)
    a, b = map(int, ab)
    n = 0
    xs = ['']
    # construct all the possible palindromes
    # only need half the length (loop max is len(str(10**100))/2 = 50)
    # start at 1 (TODO: lower bound would be at least sqrt(a))
    for l in range(1, lb+1): # int(lb/2)+1
        xst = [] # store palindromes generated below in own list, otherwise xs gets mixed up
        for x in xs: # 10**25 still too large
            for i in range(0, 10):
                s = str(i)
                xx = ''
                if l==1: # 0 to 9
                    xx = s
                elif l==2:
                    xx = s+s
                else:
                    xx = s+x+s
                # xx is a palindrome now -> add it to the list
                xst.append(xx)
                # check constraints
                if i==0: continue # no leading zeros
                sq = int(xx)**2
                if sq<a: continue # out of bounds
                if sq>b: return n # done
                # check if its square is also a palindrome
                if p(str(sq)): 
                    n += 1
                    # print(sq)
        xs.extend(xst)
        xs = list(filter(lambda x: len(x)==l, xs))
    return n

for line in f:
    t = fileinput.lineno()-1
    n = nfs(line.strip().split())
    print("Case #%s: %s"%(t,n))
