f = file("in1.py", "r").read().split("\n")
cases = int(f[0])
for i in range(cases):
    out = []
    stuff = f[1+10*i:11+10*i]
    sq1 = stuff[1:5]
    sq2 = stuff[6:11]
    guess1 = stuff[0]
    guess2 = stuff[5]
    sq1a = [k.split(" ") for k in sq1]
    sq2a = [m.split(" ") for m in sq2]
    pared1 = sq1a[int(guess1)-1]
    pared2 = sq2a[int(guess2)-1]
    for j in pared1:
        if j in pared2:
            out.append(j)
    if len(out) == 1:
        print "Case #" + str(i+1) +": " + out[0]
    if len(out) > 1:
        print "Case #" + str(i+1) +": Bad magician!"
    if len(out) == 0:
        print "Case #" + str(i+1) +": Volunteer cheated!"
        
            
    
