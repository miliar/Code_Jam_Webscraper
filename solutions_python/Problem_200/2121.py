
with open('B-large.in') as f:
    content = f.readlines()


f = open('output.txt', 'w')
testCase = 1

for line in content[1:]:

    N = list(line)
    
    if '\n' in N:
        N.remove('\n')
    print(N)
    
    for i in range(len(N)-1,0,-1):
        if N[i - 1] > N[i]:
            N[i] = '9'
            N[i - 1] = chr(ord(N[i - 1]) - 1)
    
    for i in range(0,len(N)):
        if N[i] =='9':
            for j in range(i+1, len(N)):
                N[j] = '9'
            break        
        
    
    print(N)
    
    ret = ""
    if N[0] != '0':
        ret = ret + N[0]
    for i in range(1,len(N)):
        if N[i - 1] > N[i]:
            ret = ret + N[i-1]
        else:
            ret = ret + N[i]
    
        
    f.write("Case #" + str(testCase) + ": " + ret + "\n")
    testCase = testCase + 1
   
f.close()