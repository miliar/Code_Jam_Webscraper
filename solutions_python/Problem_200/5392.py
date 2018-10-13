def checker(n):
    s = str(n)
    is_tidy = True
    i=0
    if ( len(s) == 1 ):
        return True
    while i < len(s)-1:
        if( int(s[i]) > int(s[i+1]) ):
            is_tidy = False
            return is_tidy
        i = i +1
    return is_tidy
    
    
c = checker(131)
print(c)


def solver(n): #finds the largest tidy number given an N value
    largest = 1
    for i in range(n+1):
        if(checker(i)):
            largest = i
    return largest
    
#d = solver(111111111111111110)
#print(d)

res = []
file = open("B-small-attempt1.in", "r")
fh = open("output.txt","w")
for line in file:
    res.append(solver(int(line)))
    
res.pop(0)    
s = ""
for i in range(len(res)):
    s = "Case #"+str(i+1)+": "+str(res[i])+"\n"
    fh.write(s)
    
file.close()
fh.close()