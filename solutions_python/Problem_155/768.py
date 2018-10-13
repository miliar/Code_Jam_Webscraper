boo = 0
answers = []

people = 0
ringers = 0
with open('ovationinput.txt', 'r') as fi:
    for line in fi:
        if boo==0:
            boo = 1
        else:
            vals = line.split()
            people = 0
            ringers = 0
            for i in range(len(vals[1])):
                curr = int(vals[1][i])
                if i > (people+ringers):
                    ringers += (i-(people+ringers))
                people += curr
            answers.append(ringers)
    fi.close

val = 1
with open('ovationoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val = val+1
    fi.close
