def maxnosur(n):
    n -= n /3
    n -= n /2
    return n


def minnosur(n):
    return n/3

def maxsur(n):
    mxns = maxnosur(n)
    mnns = minnosur(n)
    otro = n - mxns - mnns
    if otro > 0 and otro==mxns:
       mxns += 1

    return mxns

dict_maxsur = {}
dict_maxnosur = {}

for i in range(31):
    mn = minnosur(i)
    mx = maxnosur(i)
    otro = i - mn - mx

    mxs = maxsur(i)
    mns = (i-mxs)/2
    otros = i - mxs- mns

    dict_maxnosur[i] = mx
    dict_maxsur[i] = mxs

#    df = mxs - mns
#    if mxs - otros > df:
#       df = mxs - otros
#    print i, "->",mn, otro, mx, "  ",mxs, mns,otros," ", df

n = int( input() )
# print "Lei n = ", n

for i in range(n):
    values = raw_input().split()
    N = int(values[0])
    S = int(values[1])
    p = int(values[2])
    v = []
    for j in range(3,len(values)):
        v.append(int(values[j]))

    v = sorted(v,reverse=True)
#    print "case ", i+1, " sorted values ", v
    c = 0
    for val in v:
        if dict_maxnosur[val] >= p:
           c += 1
#           print "case ", i+1, " value ", val, " ~ ", dict_maxnosur[val], " >= ", p, " -> ", c
        else:
           if S > 0 and dict_maxsur[val] >= p:
              c += 1
              S -= 1
#              print "case ", i+1, " value ", val, " ~ ", dict_maxsur[val], " >= ", p, " -> ", c, " **"
    print "Case #"+str(i+1) + ":", c



