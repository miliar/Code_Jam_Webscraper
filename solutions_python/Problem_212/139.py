level = __file__.split("\\")[-1][0]
file_is_small = 0
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

def test_case():
    fresh = 0
    [N,P] = [int(x) for x in input_file.readline().split()]
    mod = [0] * P
    groups = [int(x) for x in input_file.readline().split()]
    for g in groups:
        mod[g % P] += 1
    fresh += mod[0]
    mod[0] = 0
    for i in xrange(1,P):
        c = mod[i]
        while(mod[i] > 0 and c > 0):
            mod[i] -= 1
            if(mod[P-i] > 0):
                mod[P-i] -= 1
                fresh += 1
            else:
                mod[i] += 1
            c -= 1
    k = sum(mod)
    if(P == 4):
        k += mod[2]
    fresh += k/P + ((k % P) > 0)
        
    return fresh

T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    print out
    output_file.write(out + "\n")
    
input_file.close()
output_file.close()
