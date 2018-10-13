lines = [l for l in file("in")][1:]

case = 0
for x in zip(lines[::2], lines[1::2]):
        case +=1 
        one = [int(a) for a in x[0].split(" ")]
        queue = [int(a) for a in x[1].split(" ")] #people in line
        
        R = one[0] # number of times run
        k = one[1] # size of coaster 

        euros = 0
        runs = 0
        position = 0

        while runs < R:
                people = 0
                groups = 0
                while True:
                        people += queue[position%len(queue)]
                        groups += 1
                        if people > k or groups > len(queue): 
                                people -= queue[position%len(queue)]
                                break
                        position +=1
                runs += 1
                euros += people

        print "Case #%d: %d" % (case, euros)
