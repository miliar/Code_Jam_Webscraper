import fileinput

C = 500
F = 4
X = 2000

i=0
for line in fileinput.input():
    if i==0:
        i+=1
        continue
    lineint = [float(j) for j in line.split()]
    C=lineint[0]
    F = lineint[1]
    X = lineint[2]

    ans = X
    newans = X/2
    coeff = 0
    n=1

    while newans < ans:
    
        coeff += C/(2+F*(n-1))
        t = (X)/(2+F*n) + coeff
        n+=1
        ans = newans
        newans = t

    print("Case #" + str(i) + ": " + str(ans))
    i+=1