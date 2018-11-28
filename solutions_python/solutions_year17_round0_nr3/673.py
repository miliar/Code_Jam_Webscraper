import Queue

level = __file__.split("\\")[-1][0]
file_is_small = 0
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")


def test_case():
    [n,k] = [int(x) for x in input_file.readline().split()]
    arr = [n]
    d = dict()
    d[n] = 1
    for e in arr:
        c = d[e]
        i = e/2
        j = (e-1)/2
        for x in [i,j]:
            if(x in d):
                d[x] += c
            else:
                if(not x == 0):
                    d[x] = c
                    arr.append(x)
    out = []
    for e in arr:
        if(d[e] >= k):
            return "{0} {1}".format(e/2,(e-1)/2)
        else:
            k -= d[e]
    
    
    
T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    #print out
    output_file.write(out + "\n")
input_file.close()
output_file.close()
