lines = [i.rstrip() for i in open("A-large.in", "r").readlines()]

case = 1
for line in lines[1:]:
    split = line.split(" ")
    size = int(split[0])
    flag = ""
    orange = 1
    blue = 1
    time = 0
    tmp = 0

    for i in range(size):
        idx = 1 + i * 2
        man = split[idx]
        pos = int(split[idx + 1])

        if man == flag:
            if man == "O":
                t = abs(pos - orange) + 1
                orange = pos
            else:
                t = abs(pos - blue) + 1
                blue = pos

            time += t
            tmp += t
        else:
            if man == "O":
                t = abs(pos - orange)
                orange = pos
                flag = "O"
            else:
                t = abs(pos - blue)
                blue = pos
                flag = "B"

            if t == 0 or t < tmp:
                time += 1
                tmp = 1
            else:
                time += t - tmp + 1
                tmp = t - tmp + 1
                
    print "Case #%d: %d" % (case, time)
    case += 1
                
            
            


    
        
    
    
