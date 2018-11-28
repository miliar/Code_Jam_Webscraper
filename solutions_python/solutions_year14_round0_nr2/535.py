from collections import deque


input = open('./B-large.in', 'r').readlines()
output = open('./B-large.out', 'w') 

inputQueue = deque(input)
testCases = int(inputQueue.popleft())
for i in range(0, testCases):
    outputString = "Case #"+str(i+1)+": "
    input = inputQueue.popleft().split()
    c = float(input[0])
    f = float(input[1])
    x = float(input[2])
    minimum = x / 2
    current = float("inf")
    elapsed = float(0)
    cps = 2
    while True:
        #calc elapsed time to buy a farm
        buildingTime = c / cps
        cps += f
        #calc remaining time
        remainingTime = x / cps
        current = elapsed + buildingTime + remainingTime
        if current <= minimum:
            elapsed += buildingTime
            minimum = current
        else:
            break
    
    outputString += str(minimum)+"\n"
    output.write(outputString)
    print(i)
output.close()
    
    
#C: cookies needed for a Farm
#F: extra cookies per second
#X: goal cookie amount