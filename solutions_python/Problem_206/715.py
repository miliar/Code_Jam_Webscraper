boo = 0
answers = []

d = 0
n = 0
horses = []

with open('firstinput.txt', 'r') as fi:
    for line in fi:
        if boo==0:
            boo = 1
        elif n > 0:
            [a, b] = line.split()
            a = int(a)
            b = int(b)
            horses.append((a,b))
            n -= 1

            if n == 0:
                #print horses
                maxtime = 0.0
                for horse in horses:
                    rate = (float(d)-float(horse[0]))/(float(horse[1]))
                    if rate > maxtime:
                        maxtime = rate

                answers.append(d/maxtime)
                
        else:
            [d, n] = line.split()
            d = int(d)
            n = int(n)
            #print ('d', d, n)
            horses = []
            
                       
    fi.close

val = 1
with open('firstoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str("%.6f" % answer) + '\n')
        val = val+1
    fi.close
