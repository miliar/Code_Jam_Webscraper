fB = open('C:\Documents and Settings\Protean\Desktop\B-large.in','r')
fOUT = open('C:\Documents and Settings\Protean\Desktop\output_B_large.txt','w')

N_cases = int(fB.readline())
Nc = range(N_cases)

for x in Nc[:]:

    Required_A = 0
    Required_B = 0
    Now_at_A = 0
    Now_at_B = 0

    Turn_time = int(fB.readline())
    
    temp = fB.readline()

    N_A = N_B = ''

    i = 0

    while temp[i] != ' ':    #Running through the digits of N_A
        N_A = N_A + temp[i]
        i = i + 1
    i = i + 1                #Proceeding past the space.
    
    while temp[i] != '\n':   #Running through the digits of N_B
        N_B = N_B + temp[i]
        i = i + 1

    N_A = int(N_A)
    N_B = int(N_B)
    
    Na = range(N_A)
    Nb = range(N_B)

    Times_A1 = []
    Times_B1 = []
    Times_A2 = []
    Times_B2 = []
    
    for y in Na[:]:

        Time_line = fB.readline()
        Times_A1 = Times_A1 + [(60*int(Time_line[0:2])+int(Time_line[3:5]))]
        Times_A2 = Times_A2 + [(60*int(Time_line[6:8])+int(Time_line[9:11])) + Turn_time]

    Times_A1 = Times_A1 + [1441]
    Times_A2 = Times_A2 + [1441]
    Times_A1.sort()
    Times_A2.sort()
        
    for y in Nb[:]:

        Time_line = fB.readline()
        Times_B1 = Times_B1 + [(60*int(Time_line[0:2])+int(Time_line[3:5]))]
        Times_B2 = Times_B2 + [(60*int(Time_line[6:8])+int(Time_line[9:11])) + Turn_time]

    Times_B1 = Times_B1 + [1441]
    Times_B2 = Times_B2 + [1441]
    Times_B1.sort()
    Times_B2.sort()

    i = j = 0

    while (i < N_A):
        if(Times_A1[i] < Times_B2[j]):
            if Now_at_A > 0:
                Now_at_A = Now_at_A - 1
            else:
                Required_A = Required_A + 1
                #print 'Demand at A', Times_A1[i], Times_B2[j]
            i = i + 1
        elif (Times_A1[i] == Times_B2[j]):
            #print 'Touch and go'
            i = i + 1
            j = j + 1
        else:
            Now_at_A = Now_at_A + 1
            j = j + 1

    i = j = 0

    while (i < N_B):     
        if(Times_B1[i] < Times_A2[j]):
            if Now_at_B > 0:
                Now_at_B = Now_at_B - 1
            else:
                Required_B = Required_B + 1
                #print 'Demand at B', Times_B1[i], Times_A2[j]
            i = i + 1
        elif (Times_B1[i] == Times_A2[j]):
            #print 'Touch and go'
            i = i + 1
            j = j + 1
        else:
            Now_at_B = Now_at_B + 1
            j = j + 1
            
    temp = 'Case #' + str(x+1) + ': ' + str(Required_A) + ' ' + str(Required_B) + '\n'
    print temp
    fOUT.write(temp)
fB.close()
fOUT.close()
