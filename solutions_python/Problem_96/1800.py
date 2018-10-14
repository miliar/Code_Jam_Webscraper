finput = open('B-small-attempt3.in','r')
cases = int(finput.readline())
foutput = open('output2','w')

for case in range(cases):
    line = finput.readline()
    array = line.split(' ')
    n_googlers = int(array[0])
    n_surprises = int(array[1])
    p_output = int(array[2])
    totals = []
    output = 0

    for i in range(0,n_googlers):
        totals.append(int(array[i+3]))

    length = len(totals)

    for index in range(0,length):
        maximum = 0
        if totals[index] % 3 == 0:
            if n_surprises > 0 and not totals[index] == 0:
                maximum = totals[index] / 3
                if maximum < p_output:
                    n_surprises-=1
                    maximum = ( totals[index] / 3 ) + 1
                if maximum < p_output:
                    n_surprises+=1
            else:
                maximum = totals[index] / 3

        elif totals[index] % 3 == 1:
            maximum = int( totals[index] / 3 ) + 1

        else:
            if n_surprises > 0:
                maximum = int( totals[index] / 3 ) + 1
                if maximum < p_output:
                    n_surprises-=1
                    maximum = int( totals[index] / 3 ) + 2
                if maximum < p_output:
                    n_surprises+=1
            else:
                maximum = int( totals[index] / 3 ) + 1

        if totals[index] == 0:
            maximum = 0

        if maximum >= p_output:
            output+=1

    beautyoutput = 'Case #'+str(case+1)+': '+str(output)+'\n'
    foutput.write(beautyoutput)
    
finput.close()
foutput.close()
