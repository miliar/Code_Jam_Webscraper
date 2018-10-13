f = open(r"/home/cr0byt3ch/Downloads/C-small-attempt0.in")
g = open("/home/cr0byt3ch/Desktop/output6.out", 'w')

from math import sqrt

case_no = int(f.readline().rstrip('\n'))

def square():
    k = f.readline().rstrip().partition(' ')
    lim_1 = int(k[0])
    lim_2 = int(k[2]) + 1
    
    count = 0
    for i in range(lim_1,lim_2):
        if sqrt(i)//1 == sqrt(i) and str(int(sqrt(i))) == str(int(sqrt(i)))[::-1]:
            s = str(i)
            if s == s[::-1]:
                count = count + 1
    return count

for i in range(case_no):
    ans = square()
    g.writelines("Case #"+str(i +1)+": " + str(ans)+'\n')
g.close()
f.close()
    
    
