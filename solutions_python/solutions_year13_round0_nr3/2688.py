infile = open("DATA.txt")
infile = infile.readlines()
x = int(infile[0])
outfile = open("out.txt", "w")
def ispalindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False
for i, v in enumerate(infile[1:]):
    v = v.strip().split()
    out = 0
    for ii in range(int(v[0]), int(v[1])+1):
        if ispalindrome(str(ii)):
            if int(ii**0.5) == (ii**0.5):
                if ispalindrome(str(int(ii**0.5))):
                    out += 1
    outfile.write( "Case #%i: %i\n"%(i+1, out) )
outfile.close()