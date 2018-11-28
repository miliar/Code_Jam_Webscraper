import math

def pileize(height, newheight):
    return int(math.ceil(float(height)/float(newheight))-1)

boo = 0
answers = []
with open('pancakeinput.txt', 'r') as fi:
    for line in fi:
        if boo == 0:
            boo = 1
        elif boo == 1:
            boo = 2
        else:
            boo = 1
            line = line.strip()
            vals = line.split(' ')

            for i in range(len(vals)):
                vals[i] = int(vals[i])

            maximum = max(vals)
            minimum = maximum+0

            for i in range(1,maximum+1):
                steps = 0
                for val in vals:
                    steps += pileize(val, i)
                if (i+steps < minimum):
                    minimum = (i+steps)
            
            answers.append(str(minimum))
    fi.close

val = 1
with open('pancakeoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val += 1
    fi.close
