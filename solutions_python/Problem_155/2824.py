fInput = open("A-large.in", 'r')
fOutput = open("A-large.out", 'w')

num_cases = int(fInput.next())

for case in range(1,num_cases+1):
    audience= map(int, fInput.next().split()[1])
    clappers = 0
    extras = 0
    for shynessLevel in range(len(audience)):
        extrasLevel = max(0, shynessLevel - clappers)
        clappers += audience[shynessLevel] + extrasLevel
        extras += extrasLevel        
    out_str = str(extras)
    fOutput.write("Case #{0}: ".format(case) + out_str + "\n")    
fInput.close()
fOutput.close()