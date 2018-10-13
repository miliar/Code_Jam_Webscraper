def maxTidy(N):
    isTidy = True
    
    N = str(N)
    
    n = ""
    i = 0
    while i < len(N)-1:
        if int(N[i]) > int(N[i+1]):
            isTidy = False
            break
        i += 1

    if(isTidy):
        return N
    
    while i > 0:
        if int(N[i-1]) <= int(N[i])-1:
            break
        i -= 1

    for digit in range(i):
        n += N[digit]

    n += str(int(N[i])-1)

    for digit in range(i+1, len(N)):
        n += "9"

    return str(int(n))

def main():
    infile = open("B-large.in", "r")
    outfile = open("B-large.out", "w")
    T = int(infile.readline())
    for i in range(T):
        N = int(infile.readline())
        outfile.write("Case #"+str(i+1)+": "+maxTidy(N)+"\n")

    infile.close()
    outfile.close()
