import math

def isPali(num):
    ret = 0
    temp = num
    while temp > 0:
        ret = 10 * (ret+temp%10)
        temp = int(temp/10)
    ret = int(ret/10)
    if ret == num:
        return True
    return False

def main():
    f = open('C-small.in','r')
    g = open('output3.txt','w')
    n = int(f.readline().strip('\n\r'))
    for i in range(n):
        l = f.readline().strip('\n\r').split()
        l[0] = int(l[0])
        l[1] = int(l[1])
        cases = 0
        for j in range(l[0],l[1]+1,1):
            root = math.sqrt(j)
            if root == int(root):
                if isPali(j) == True:
                    if isPali(root) == True:
                        cases += 1
        string = "Case #" + str(i+1) + ": " + str(cases) + "\n"
        g.write(string)
    f.close()
    g.close

main()
