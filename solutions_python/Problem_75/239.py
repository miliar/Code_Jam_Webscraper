"""
QR2011 B
http://code.google.com/codejam/contest/dashboard?c=975485#s=p1
"""

def Magicks(result, combine, opposed):
    if len(result) > 1:
        n = result[-1]
        if n in combine:
            m = result[-2]
            if m in combine[n]:
                result = result[:-2]
                result += [combine[n][m]]
                return result
        if n in opposed:
            m = opposed[n]
            if m in result[:-1]:
                result = []
                #result = result[:-result[::-1].index(m)-1]
                return result
    return result

if __name__ == "__main__":
    f = open("B-small-attempt4.in")
    T = int(f.readline())
    for t in range(T):
        combine = {}
        opposed = {}

        data = f.readline().split()
        C = int(data.pop(0))
        for i in range(C):
            a,b,c = data.pop(0)
            combine[a] = {b : c}
            combine[b] = {a : c}
        D = int(data.pop(0))
        for i in range(D):
            a,b = data.pop(0)
            opposed[a] = b
            opposed[b] = a
        N = int(data.pop(0))
        elements = data.pop(0)
                
        result = []
        for element in elements:
            result += [element]
            x = 1
            while(x > 0):
                d = len(result)
                result = Magicks(result, combine, opposed)
                x = d - len(result)
        
        print "Case #%d: [%s]" % (t+1, ", ".join(result))
