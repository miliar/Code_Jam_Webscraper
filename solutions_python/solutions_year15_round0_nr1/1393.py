
dataSet = {}
with open("A-large.in") as f:
    nbTestCase = int(f.readline())
    
    for i in range(1, nbTestCase+1):
        dataSet[i] = f.readline().split()[1]
        

def solveIt(data):

    res = 0
    sum = 0
    for rank, digit in enumerate(data):
        while sum < rank:
            sum+=1
            res+=1
        sum+=int(digit)


    return res
    
with open("out.txt", "w") as f:
    for k, data in dataSet.items():
        f.write("Case #{}: {}\n".format(k, solveIt(data)))