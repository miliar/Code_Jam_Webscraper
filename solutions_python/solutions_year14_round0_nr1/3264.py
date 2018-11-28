out = open('Aout.txt', 'w')
lines = open('A-small-attempt1.in').read().splitlines()

T = int(lines[0])
lines_per_case = 10

for case in xrange(1, T+1):
    base = lines_per_case*(case-1)+1
    guess = int(lines[base])
    rowA = map(int, lines[base+guess].split(" ")) 
    base += 5
    guess = int(lines[base])
    rowB = map(int, lines[base+guess].split(" "))
    result = set(rowA) & set(rowB)
    
    out.write("Case #"+str(case)+": ")
    if (len(result) == 1): 
        for s in result: out.write(str(s)+"\n")
    if (len(result) >  1): out.write("Bad magician!\n")
    if (len(result) <  1): out.write("Volunteer cheated!\n")
out.close()
