from sets import Set

fA = open('C:\Documents and Settings\Protean\Desktop\A-large.in','r')
fOUT = open('C:\Documents and Settings\Protean\Desktop\A\A_large_out.txt','w')

# Reading the number of cases and the number of engines.

N_cases = int(fA.readline())
Nc = range(N_cases)

# Going through the cases

for x in Nc:
    
    N_engines = int(fA.readline())
    Ne = range(N_engines)

    Engines_set = Set()

    for y in Ne:
        temp = fA.readline()
        Engines_set.add(temp)

#    print Engines_set
    
    K = 0 #Stores the number of switches
    
    N_inputs = int(fA.readline())
    Ni = range(N_inputs)

    Temporary = Engines_set.copy()
    
    # Reading the inputs of each case and processing them.
    for z in Ni:
        temp = fA.readline()
        if len(Temporary) > 0:
            Temporary.discard(temp)
            if len(Temporary) == 0:
                Temporary = Engines_set.copy()
                Temporary.discard(temp)
                K = K + 1
            

    print K
    temp = 'Case #' + str(x+1) + ': ' + str(K) + '\n'
    fOUT.write(temp)

fA.close()
fOUT.close()
