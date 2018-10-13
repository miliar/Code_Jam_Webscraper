input = open('A-small-attempt1.in','r')
output = open('A-small-attempt1.out','w')

cases = int(input.readline())

for case in range(cases):
    
    data = input.readline().split()
    snappers = int(data[0])
    snaps = int(data[1])

    result = "Case #" + str(case+1) +": "

    #initialise array containing pairs, 0/1 for OFF/ON and 0/1 for unpowered/powered
    chain = [[0,0] for snapper in range(snappers)]
    #first snapper is connected to power
    chain[0][1] = 1

    for snap in range(snaps):
        for snapper in range(snappers):
            if (chain[snapper][1] == 1):
                if (chain[snapper][0] == 0):
                    chain[snapper][0] = 1
                else:
                    chain[snapper][0] = 0

        for snapper in range(snappers):
            if (snapper > 0):
                if ((chain[snapper-1][1] == 1) and (chain[snapper-1][0] == 1)): 
                    chain[snapper][1] = 1
                else:
                    chain[snapper][1] = 0

    if (chain[snappers-1][0] == 1) and (chain[snappers-1][1] == 1):
        output.write(result+"ON\n")
        #print result+"ON"
    else:
        output.write(result+"OFF\n")
        #print result+"OFF"



            

