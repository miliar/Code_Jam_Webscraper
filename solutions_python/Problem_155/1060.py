infile = open("A-large.in")
outfile = open("A-large.out", 'w')

cases = int(infile.readline().strip())

for i in range(cases):
    friends = 0
    s_under = 0
    s_max, data = infile.readline().strip().split()
    for j in range(len(data)):
        if s_under >= j:
            s_under += int(data[j])
        elif int(data[j]) != 0:
            more = j - s_under
            s_under += more + int(data[j])
            friends += more
    #print friends
    result = "Case #%d: %d" %(i+1, friends)
    outfile.write(result+"\n")
infile.close()
outfile.close()
