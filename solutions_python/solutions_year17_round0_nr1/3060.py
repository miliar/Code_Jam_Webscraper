boo = 0
answers = []

with open('pancakesinput.txt', 'r') as fi:
    for line in fi:
        if boo==0:
            boo = 1
        else:
            [pcakes, flipper] = line.split()
            pcakes = list(pcakes)
            flipper = int(flipper)

            minimum = 0
            while len(pcakes) > flipper:
                if pcakes[0] == '+':
                    pcakes.pop(0)
                else:
                    minimum += 1
                    #flip
                    j = 0
                    while j < flipper:
                        if pcakes[j] == '+':
                            pcakes[j] = '-'
                        else:
                            pcakes[j] = '+'
                        j += 1

            if len(pcakes) == flipper:
                if pcakes[0] == '-':
                    minimum += 1
                    j = 0
                    while j < flipper:
                        if pcakes[j] == '+':
                            pcakes[j] = '-'
                        else:
                            pcakes[j] = '+'
                        j += 1


            while len(pcakes) > 0:
                if pcakes[0] == '+':
                    pcakes.pop(0)
                else:
                    break
                
            if len(pcakes) == 0:
                answers.append(minimum)
            else:
                answers.append('IMPOSSIBLE')            
    fi.close

val = 1
with open('pancakesoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val = val+1
    fi.close
