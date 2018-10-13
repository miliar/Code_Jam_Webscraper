file = open("A-large.in", "r")

out = open("A-large.out", "w")

cases = int(file.readline())


for case in range(cases):
    line = file.readline().replace("\n", "").split(" ")
    gigapan = list(line[0])
    
    # set pacakes to 0 / 1
    for i in range(len(gigapan)):
        if gigapan[i] == '+':
            gigapan[i] = 1
        else:
            gigapan[i] = 0
    
    flippersize = int(line[1])
    
    print("You have "+str(gigapan)+" | flippersize: "+str(flippersize))
    
    flips = 0
    
    while True:
        
        print("-------------")
        print(gigapan)
        
        
        
        if gigapan.count(0) == 0:
            print("hurrray >> you need " + str(flips))
            out.write("Case #" + str(case+1) + ": "+str(flips)+"\n")
            break
        #get most left 0 of array
        flipperstart = 0
        while gigapan[flipperstart] != 0:
            flipperstart += 1
        
        if flipperstart > len(gigapan) - flippersize:
            #cant solve problem
            print("IMPOSSIBLE")
            out.write("Case #" + str(case+1) + ": IMPOSSIBLE\n")
            break
        
        print("flipping at "+str(flipperstart))
        
        
        
        #flip values
        for i in range(flippersize):
            if gigapan[flipperstart + i] == 0:
                gigapan[flipperstart + i] = 1
            else:
                gigapan[flipperstart + i] = 0
        
        flips += 1
        
        
out.close()
file.close()