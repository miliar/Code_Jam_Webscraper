file = open('M:\in.in')
output = open('M:\output.out', 'w', 0)
N = file.readline()
for i in range(1, int(N) + 1):
    line = file.readline()
    A, B = line.split()
    A = long(A)
    B = long(B)
    has = 0
    has2 = 0
    for n in range(A, B+1):
        str1 = str(n)
        for m in range(n+1, B+1):
            str2 = str(m)
            if(sorted(str1) == sorted(str2)):
                for j in sorted(range(1, len(str1)+1), reverse=True):
                    if(str1.rfind(str2[0:j]) + j == len(str1)):
                        if(str1[0:str1.rfind(str2[0:j])] == str2[j:]):
                            has += 1
                            break
    output.write("Case #{}: {}\n".format(i, has))
                        
                
                
