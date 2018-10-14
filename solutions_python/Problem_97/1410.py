infile = open('in-recycledNumbers.txt','r')
outfile = open('out-recycledNumbers.txt','w')
n = int(infile.readline())

for ni in range(1, n+1):
    nums = infile.readline().split()
    a = int(nums[0])
    b = int(nums[1])
    anselems = []
    for i in range(a,b+1):
        stri = str(i)
        leni = len(stri)
        for j in range(leni):
            ishift = int(str(stri[j:]+stri[:j]))
            if(a <= i and i < ishift and ishift <= b and (i,ishift) not in anselems):
                anselems.append((i,ishift))
            
    outfile.write('Case #' + str(ni) + ": " + str(len(anselems)) + "\n")

outfile.close()
infile.close()
