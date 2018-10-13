fInput = open("A-small-attempt0.in", 'r')
fOutput = open("A-small-attempt0.out", 'w')

num_cases = int(fInput.next())

for case in range(1,num_cases+1):
    row1 = int(fInput.next())
    for i in range(1,5):
        if i == row1:
            candidates = set(fInput.next().split())
        else: 
            fInput.next()
    row2 = int(fInput.next())
    for i in range(1,5):
        if i != row2:
            fInput.next()
        else:
            candidates = candidates.intersection(set(fInput.next().split()))
    if len(candidates) == 0:    
        out_str = "Volunteer cheated!"
    elif len(candidates) == 1:
        out_str = candidates.pop()
    else:
        out_str = "Bad magician!"            
    fOutput.write("Case #{0}: ".format(case) + out_str + "\n")    
fInput.close()
fOutput.close()
