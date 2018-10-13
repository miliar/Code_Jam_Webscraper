import math

def is_pali(n):
    s = str(n)
    l = len(s)
    #print "N: ",n , " S ", s
    for i in range(l/2):
        if not s[i]==s[l-i-1]:
            return False
    return True
def find_palis(lis):
    c = 0
    for num in lis:
        if is_pali(num):
            if is_pali(num**2):
                c+=1
    return c
            
            
def find_squares(a,b):
    s = int(math.ceil(a**0.5))
    l = []
    while s**2 <= b:
        l.append(s)
        s+=1
    return l

def square():
    inp = "C-small-attempt0.in"
    out = "C-small-attempt0-OUT.txt"
    f = open(inp, 'r')
    fo = open(out, 'w')
    num_lines = f.readline()
    for j in range(int(num_lines)):
        
        s = f.readline().replace("\n","").split(" ")
        squares = find_squares(int(s[0]),int(s[1]))
        palis_nume = find_palis(squares)
        print "The count is", palis_nume
        fo.write("Case #{0}: {1}".format(j+1,palis_nume))
           
        fo.write("\n")
square()
