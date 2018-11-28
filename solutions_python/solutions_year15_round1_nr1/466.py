f = open('AInput.txt')
lines = f.readlines()
f.close()


output = open('AOutput.txt','w')

for i in range(int(lines[0])):
    arg1 = int(lines[2*i+1])
    arg2 = lines[2*i+2].split()
    mush = []
    for item in arg2:
        mush.append(int(item))
        
    print mush
    num_eaten = 0
    for j in range(len(mush)-1):
        first = mush[j]
        second = mush[j+1]
        if(second < first):
            num_eaten += first - second
    
    min1 = num_eaten
    
    num_eaten = 0
    largest_gap = 0
    rate = 0
    gap = 0
    for j in range(len(mush)-1):
        first = mush[j]
        second = mush[j+1]
        if(second < first):
            gap = first - second
            if(gap > largest_gap):
                largest_gap = gap
    for j in range(len(mush)-1):
        first = mush[j]
        second = mush[j+1]
        if(first > second):
            if(first >= largest_gap):
                num_eaten += largest_gap #puts mush on plate to add
            else:
                num_eaten += first #max amount 
        else:
            if(first >= largest_gap):
                num_eaten += largest_gap #puts mush on plate to add
            else:
                num_eaten += first #max amount 
            
            
    min2 = num_eaten
    output.write("Case #")
    output.write(str(i+1))
    output.write(": ")
    output.write(str(min1))
    output.write(" ")
    output.write(str(min2))
    output.write("\n")

output.close() 