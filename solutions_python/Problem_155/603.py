
debug = False

def dep(msg):
    if debug:
        print msg

def preprocess(input_data):
    result = None
    split_data = input_data.split(" ")

    result = {"n": int(split_data[0]), "S": [int(i) for i in split_data[1]]}
    #dep(result)
    return result

def algo(pd):
    result = 0

    n = pd['n']
    S = pd['S']

    cul_a = []
    cul_a.append(S[0])
    for i in range(1,n+1):
        #print "S[%d]: %d,  %d - cul_a[%d]: %d" %(i, S[i], i, cul_a[i-1], i-cul_a[i-1])
        if S[i]>0 and (i-cul_a[i-1]) > 0:
            add = (i-cul_a[i-1])
            cul_a[i-1] += add
            result += add
        cul_a.append(cul_a[i-1]+S[i])

    return result

def answer(ro, i):
    result = "Case #%d: %s" %(i+1, str(ro))
    dep("result: " + result)
    return result

"""main"""

N = int(raw_input())
dep("N: %d" %N)

result = []
out = ''

for i in range(0, N):
    result.append( answer( algo( preprocess(raw_input()) ), i) )

dep("=================")
out = '\n'.join(result)
print out

