level = __file__.split("\\")[-1][0]
file_is_small = 0
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

def test_case():    
    [D,N] = [int(i) for i in input_file.readline().split()]
    D = float(D)
    speed = -1
    for horse in xrange(N):
        [pos,S] = [float(i) for i in input_file.readline().split()]
        if(pos < D):
            time = (D-pos)/S
            if(speed < 0):
                speed = D/time
            else:
                speed = min(speed,D/time)
    return speed       

T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    #print out
    output_file.write(out + "\n")
    
input_file.close()
output_file.close()
