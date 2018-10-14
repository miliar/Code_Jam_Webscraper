import math

inputFile = "inputC.txt"
outputFile = "outputC1.txt"

f = open(inputFile, "r")
f.readline()
wf = open(outputFile, "w")

def bathroom(n, k):

    ans = n - (k - 1)
    denom = math.floor(math.log(k, 2))
    denom = math.pow(2, denom)
    ans = ans/denom

    if (ans).is_integer():
        ans = ans - 1
    else:
        ans = math.floor(ans)

    if(ans/2).is_integer():
        return(int(ans/2), int(ans/2))
    else:
        return(int(math.ceil(ans/2)), int(math.floor(ans/2)))




testCase = 1
for line in f:
    n = int(line.split()[0])
    k = int(line.split()[1])

    output = bathroom(n,k)
    wf.write("Case #" + str(testCase) + ": " + str(output[0]) + " " + str(output[1]) + "\n")
    testCase += 1

f.close()
wf.close()