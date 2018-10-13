with open('C-small-1-attempt1.in') as f:
    content = f.readlines()


f = open('output.txt', 'w')
testCase = 1

for line in content[1:]:

    split = line.split(' ')
    N = int(split[0])
    K = int(split[1])
        
    tmp = [N]
    
    for i in range(0,K - 1):
        item = tmp.pop(0)
        tmp.append(int(item/2))
        if item % 2 == 1:
            tmp.append(int(item/2))
        else:
            tmp.append(int(item/2)-1)
        tmp.sort(reverse=True)
    
    last = tmp.pop(0)
    maxx = int(last/2)
    minx = int(last/2)
    if last % 2 == 0:
        minx = minx - 1
    
    f.write("Case #" + str(testCase) + ": " + str(maxx) + " " + str(minx) + "\n")
    testCase = testCase + 1
   
f.close()