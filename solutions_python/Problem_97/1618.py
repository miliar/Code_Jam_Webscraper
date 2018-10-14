#define functions
def isRecycled(n, m):
    A = str(n)
    B = str(m)
    length = len(A)
    if len(A)!=len(B) or length==1: return False

    
    for i in range(1, length):
        test = A[-i:]+A[:length-i]

        if test[0] == '0': continue

        if test == B:
            return True
    return False

#read imput
f = open("C-small-attempt0.in", "r")
text = f.read()
f.close()

lines = text.split('\n')
cases = int(lines[0])


f = open("output.txt", "w")

for i in range(1, cases+1):
    limits = lines[i].split(' ')
    A = int(limits[0])
    B = int(limits[1])
    result = 0

    for m in range(A+1, B+1):
        for n in range(A, m):
            if isRecycled(n, m):
                result += 1

    output = "Case #"+str(i)+": "+str(result)+'\n'
    f.write(output)

f.close()
