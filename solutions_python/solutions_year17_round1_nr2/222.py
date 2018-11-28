import math

level = __file__.split("\\")[-1][0]
file_is_small = 1
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

low = 0.9
high = 1.1
def bounds(fl):
    return [int(math.ceil(fl/high)), int(math.floor(fl/low))]
def test_case():
    [N,P] = [int(x) for x in input_file.readline().split()]
    portion = [float(x) for x in input_file.readline().split()]
    packages = []
    for i in xrange(N):
        packages.append([float(x) for x in input_file.readline().split()])
        packages[i].sort()
        
    total = 0
    
    if(N == 1):
        for i in packages[0]:
            ratio = float(i)/portion[0]
            b = bounds(ratio)
            if(b[0] <= b[1]):
                total+=1
    else:
        j = 0
        for i in packages[0]:
            ratio = float(i)/portion[0]
            b = bounds(ratio)
            for j in xrange(len(packages[1])):
                ratio2 = float(packages[1][j])/portion[1]
                b2 = bounds(ratio2)
                b2[0] = max(b[0],b2[0])
                b2[1] = min(b[1],b2[1])
                if(b2[0] <= b2[1]):
                    total +=1
                    packages[1].remove(packages[1][j])
                    break         
    
    return total
    
T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    print out
    output_file.write(out + "\n")
    
input_file.close()
output_file.close()
