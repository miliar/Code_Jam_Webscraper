inputFile = open('B-large.in', 'r')
file1 = inputFile

file2 = open("CookieAnswer.txt", 'w')
## function given C = cost of extra farm, F = extra rate, and X = Goal##

#n = current number of cookies
#r = current cookie rate

####

def cookie_function(list_cfx, r=2.000000):
    c, f, x = list_cfx
    c = float(str(list_cfx[0]))
    f = float(str(list_cfx[1]))
    x = float(str(list_cfx[2]))
    
    t = 0.00
    n = 0.00

    while ((c/r) +(x)/(r+f)) < (x/r): # buy time < no buy time
        t += c/r
          #  t += ((x-c)/(r+f) 
        r += f
    t += (x)/r
    n = t*r
    
    return t

ans = cookie_function([30.0, 2.0, 100.0]) 



### Given their input, Iterate test case things ###

caseNumber = int(file1.readline())

for caseN in range(caseNumber):
    
    string1 = file1.readline()
    string1 = string1[:string1.index("\n")]

    list1 = string1.split(' ')
    N = caseN + 1
    file2.write("Case #"+str(N)+ '' +  ":" + ' ' + str('%.7f' % cookie_function(list1)) + '\n')

file2.close()
