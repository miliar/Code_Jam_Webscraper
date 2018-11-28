import math

def ispalindrome(x):
    if str(x) == str(x)[::-1]: 
            return True
    return False

def presmetaj(l1,l2):
    print l1, l2
    palindromes = 0
    print (int(math.ceil(math.sqrt(l1))), int(math.floor(math.sqrt(l2))))
    for j in range(int(math.ceil(math.sqrt(l1))), int(math.floor(math.sqrt(l2)))+1):
        if ispalindrome(j) and ispalindrome(j*j):
            palindromes=palindromes+1
    return palindromes    

def presmetajs(s):
    ns = [int(x) for x in s.split()]
    l1 = ns[0]
    l2 = ns[1]
    return presmetaj(l1,l2)

f = open('./input', 'rU')
f2 = open('./output', 'w')
r = ''
for i in range(int(f.readline())):
    r+='Case #' + str(i+1) + ': ' + str(presmetajs(f.readline())) + '\n'
f2.write(r)
f.close()
f2.close()