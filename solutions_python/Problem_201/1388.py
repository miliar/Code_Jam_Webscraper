import math
def bath(n,k):
    arr = [n]
    minimum = 0
    maximum = 0
    for i in range(k):
        maxi = max(arr)
        idx = arr.index(maxi)
        if maxi % 2 == 0:
            minimum = maxi//2 - 1
            maximum = maxi//2
        else:
            minimum = (maxi - 1)//2
            maximum = (maxi - 1)//2

        arr[idx] = minimum
        arr = arr[:idx+1] + [maximum] + arr[idx+1:]
    return (maximum,minimum)

def bath2(n,k):
    levels = math.floor(math.log(k,2))
    minimum = [n,1]
    maximum = [n,0]
    for i in range(levels):
##        print("maximum: " +str(maximum))
##        print("minimum: " +str(minimum))
        if minimum[0] == maximum[0]:
            value = minimum[0]
            if minimum[0] % 2 == 0:
                maximum[0] = value /2
                minimum[0] = maximum[0] - 1
                maximum[1] = minimum[1]
            else :
                minimum[0] = maximum[0] = (value -1 )/2
                minimum[1] *= 2
        else:
            minVal = minimum[0]
            maxVal = maximum[0]
            if maxVal % 2 == 0:
                maximum[0] /= 2
                minimum[0] = maximum[0] - 1
                minimum[1] *= 2
                minimum[1] += maximum[1]
            else:
                maximum[0] = (maximum[0]-1)/2
                minimum[0] = maximum[0] - 1
                maximum[1] *= 2
                maximum[1] += minimum[1]

    index = k - 2**levels + 1
    if maximum[1] < index:
        value = minimum[0]
    else:
        value = maximum[0]
    return (math.ceil((value-1)/2),math.floor((value-1)/2))

def f(inFile,outFile):
    T = int(inFile.readline())
    for i in range(T):
        line = inFile.readline()
        split = line.split(' ')
        N = int(split[0])
        K = int(split[1])
        bath = bath2(N,K)
        outFile.write("Case #" + str(i+1) + ": " + str(bath[0]) + " " + str(bath[1]) + "\n")


inFile = open("C:/Users/USER/Downloads/C-small-2-attempt0.in","r")
outFile = open("C:/Users/USER/Downloads/C-small12.out","w")
f(inFile,outFile)
inFile.close()
outFile.close()

            
            
