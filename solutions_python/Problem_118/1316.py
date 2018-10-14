import math

file=open('C-small-attempt0.in','r')
wfile=open('output01','w')
number_of_cases= int(file.readline())
counter=0

def is_palindrome(x):
    in_str=str(x)
    rev_str=in_str[::-1]
    return in_str==rev_str

for i in xrange(number_of_cases):
    counter=0
    in_lst=file.readline().split()
    
    lb=int(math.sqrt(int(in_lst[0])))
    hb=int(math.sqrt(int(in_lst[1])))
    
    #print str(lb)+' '+str(hb)
    
    for j in xrange(lb,hb+1):
        if is_palindrome(j):
            if is_palindrome(j*j):
                if int(in_lst[0])<=j*j<=int(in_lst[1]):
                    counter+=1
    wfile.write('Case #'+str(i+1)+':'+str(counter)+'\n')
        
    
    
    
