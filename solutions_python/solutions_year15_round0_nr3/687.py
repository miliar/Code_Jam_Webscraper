matrix = {
    "1":{
        "1": "1", "i": "i", "j":"j", "k":"k"
    },
    "i":{
        "1": "i", "i": "-1", "j":"k", "k":"-j"
    },
    "j":{
        "1": "j", "i": "-k", "j":"-1", "k":"i"
    },
    "k":{
        "1": "k", "i": "j", "j":"-i", "k":"-1"
    }
}
def sign(x):
    if len(x)>1:
        return -1
    return 1
def extract(x):
    if len(x)>1:
        return x[1]
    return x
def calc(x, y):
    if x=="":
        return y
    sx = sign(x)
    sy = sign(y)
    ox = extract(x)
    oy = extract(y)

    n  = matrix[ox][oy]
    sn = sign(n)
    on = extract(n)

    ns = sx*sy*sn

    if ns<0:
        return "-"+on
    return on


def solve(L, X, istr): 
    
    strlen = L*X
    longstr = istr*X
    

    
    ijk   = ""  
    prev = longstr[0]
    i = 1
    while i<strlen:
        if (ijk=="" and prev=="i") or (ijk=="i" and prev=="j") :
            ijk+=prev
            prev = ""

        c = longstr[i]

        prev = calc(prev, c)

        i+=1
    if (i==strlen and ijk=="ij" and prev=="k"):    
        return "YES"

    return "NO"
if __name__ == "__main__": 
    testcases = input() 
    for caseNr in xrange(1, testcases+1): 
        LX = raw_input().split(" ")
        istr = raw_input()

        print("Case #%i: %s" % (caseNr, solve(int(LX[0]), int(LX[1]), istr)))