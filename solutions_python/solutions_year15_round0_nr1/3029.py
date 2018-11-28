f = open("A-small-attempt1.in", "r")
output = open("opera.txt", "w")

num = f.readline()
cases = f.readlines()
f.close()

for i in range(len(cases)):
    cases[i] = cases[i].replace("\n", "")
    cases[i] = cases[i].split(" ")
    
print cases

for case in cases:
    friend = 0
    aud = case[1]
    num_peeps = int(aud[0])
    
    for i in range(int(case[0])):
        if (num_peeps < (i + 1)):
            friend += ((i + 1) - num_peeps)
            num_peeps += int(aud[i + 1]) + ((i + 1) - num_peeps)
        else:
            num_peeps += int(aud[i + 1])
            
    
    print "Case #%d: %d" % (cases.index(case) + 1, friend)
    output.write("Case #%d: %d" % (cases.index(case) + 1, friend))
    output.write("\n")

output.close()