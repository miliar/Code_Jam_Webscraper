file = open("A-small-attempt5.in")
##file = open("testcases.txt")

lines = file.readlines()
newlines = []

file.close()

case = 0

for line in lines:

    if case == 0:
        pass
    else:
        data = line.split(" ")
        n = data[0]
        k = data[1]
        states = []
        for val in range(int(n)):
            states.append(-1)
        for val in range(int(k)):
            statecount = 0
            oldstates = []
            for value in states:
                oldstates.append(value)
            for state in states:
                if statecount == 0:
                    states[statecount] = state * -1
                else:
                    if oldstates[statecount-1] == -1:
                        pass
                    else:
                        oldstateon = 1
                        for oldstate in oldstates[:statecount-1]:
                            if oldstate == -1:
                                oldstateon = -1
                        if oldstateon == 1:
                            states[statecount] = state * -1
                statecount += 1

        stateon = 1

        for state in states:
            if state == -1:
                stateon = -1

        if stateon == 1:
            print "ON"
            newlines.append("Case #"+str(case)+": ON")
        else:
            print "OFF"
            newlines.append("Case #"+str(case)+": OFF")

        print states
        
    case += 1


outfile = open("output.out", "w")
for line in newlines:
    outfile.write(line+"\n")
outfile.close()

print "Output file written. Operation DONE."
