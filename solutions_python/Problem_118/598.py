pallist = []

for i in xrange(10000000): 
    num = str(i)
    palindrome = 1
    for j in xrange(len(num)/2 + len(num)%2):
        if num[j] != num[len(num)-j-1]:
            palindrome = 0
            break
    if palindrome == 1:
        pallist.append(i)
    i += 1

#print pallist

palsquares = []
for i in pallist:
    palsquares.append(i**2)

#print palsquares

fairsquare = []

for i in palsquares:
    num = str(i)
    palindrome = 1
    for j in xrange(len(num)/2 + len(num)%2):
        if num[j] != num[len(num)-j-1]:
            palindrome = 0
            break
    if palindrome == 1:
        fairsquare.append(i)

#print fairsquare

fin = file("C-large-1.in", "rU")
fout = file("C-large-1.out", "w")

nruns = int(fin.readline().strip())
for c in xrange(nruns):
    line = fin.readline().strip().split()
    rangea = int(line[0])
    rangeb = int(line[1])

    result = 0
    for i in fairsquare:
        if i >= rangea and i <= rangeb:
            result += 1

    strout = "Case #" + str(c+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
