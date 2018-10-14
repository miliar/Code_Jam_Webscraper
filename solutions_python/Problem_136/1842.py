def InputTaker(Filename):
	Input = open(Filename,"r")
	return(Input)

def CookieNumber(C,F,X):
    "Takes in F, C, X and outputs the cookie time, maybe"
    return(-2/F + X/C - 1)

def CookieTimer(C,F,X,k):
    n = CookieNumber(C,F,X)
    
    if n < 0:
        n = 0
    
    fln = int(n)
    cen = int(n) + 1
    Base = 0
    for i in range(0,fln):
        Base = Base + 1./(2 + i*F)
    FinalTime = min(C*Base + X/(2. + fln*F),C*(Base + 1./(2 + fln*F)) + X/(2. + cen*F))
    return("Case #" + str(k) + ": "+str(FinalTime))

f = InputTaker("B-large.in.txt")

size = int(f.readline())
print(size)

file = open("Output.txt", "w")

for k in range(0,size):
	b = f.readline()
	c = b.split()
	file.write(str(CookieTimer(float(c[0]),float(c[1]),float(c[2]),k+1))+"\n")

file.close

	