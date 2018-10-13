import math

out = ''
line_counter = 0

with open('input/2sample.txt', 'r') as f:
    f.readline()
    
    while 1:
        line = f.readline()
        if not line:
            break
        line_counter += 1
        result = 0
                
        line =  line.split()
        N = int(line[0])
        S = int(line[1])
        p = int(line[2])
        t = line[3:]
        
        for ti in t:
            ti = int(ti)
            
            quo = ti / 3
            rem = ti % 3
            
            # We're already there
            if quo >= p:
                result += 1
            # We can just add 1 to get there at no expense
            elif quo + 1 >= p and rem > 0:
                result += 1
            # We can add 2, but need a surprising case
            elif quo + 2 >= p and rem > 1 and S > 0:
                result += 1
                S -= 1
            # We can add 1, but need a surprising case
            elif quo + 1 >= p and S > 0 and quo > 0:
                result += 1
                S -= 1
        
        out += "Case #" + str(line_counter) + ": " + str(result) + "\n"

fo = open('q2output', "w")
fo.write(out)
fo.close()