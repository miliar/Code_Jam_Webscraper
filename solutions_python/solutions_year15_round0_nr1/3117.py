infile = open('A-large.in', 'r')
outfile = open('out.txt', 'w')

cases = int(infile.readline())
for i in range(1, cases+1):
    line = infile.readline().split()
    s_max = int(line[0])
    audience = line[1]
    standing = 0
    ans = 0
    if s_max != 0:
        for j in range(0, s_max + 1):
            if standing >= j:
                standing += int(audience[j])
            else:
                invites = j - standing
                ans += invites
                standing += int(audience[j]) + invites
    outfile.write("Case #" + str(i) + ": " + str(ans) + "\n")
                
    
infile.close()
outfile.close()
