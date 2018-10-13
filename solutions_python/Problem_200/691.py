level = __file__.split("\\")[-1][0]
file_is_small = False
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

def test_case():
    s = input_file.readline().strip()
    dig = [int(s[x]) for x in xrange(len(s))]
    L = len(dig)
    n = L
    for i in xrange(L-2,-1,-1):
        if(dig[i] > dig[i+1]):
            dig[i] -= 1
            for j in xrange(i+1,L):
                dig[j] = 9
    res = 0
    for i in dig:
        res *= 10
        res += i
    return res
    
T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    #print out
    output_file.write(out + "\n")
input_file.close()
output_file.close()
