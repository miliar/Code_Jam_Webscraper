'''
Created on Apr 14, 2012

@author: ashishgaunkar
'''
import re
input_path = '/Users/ashishgaunkar/Desktop/ws/codejam/C-small-attempt0.in'
output_path = '/Users/ashishgaunkar/Desktop/ws/codejam/C-small-attempt0.op'
    

def get_num_recycle( a, b):
    count = 0
    while (a <=b):
        m=a
        n=a+1
        
        while (n<=b):
            if is_recycled_num(m, n) :
                count +=1
            n+=1
        
        a+=1
    
    return count

    

def is_recycled_num(m, n):
    str_m = str(m)
    str_n = str(n)
    if len(str_m) ==1: # assuumption both numbers of same number of digits
        return False
    
    k = len(str_m)
    l=k
    i=0
    p=0
    #I think i am tired rt now just write simple logic, there miht be optimization possible
    while p < l:
        i -=1
        k -=1
        if str_m[i:]+str_m[:k] == str_n:
            return True
        else:
            pass
        
        p+=1
    return False
    
if __name__ == '__main__':

    fd_read = open(input_path)
    fd_write = open(output_path, 'w')
    #fd_write.write("Output\n")
    
    content = fd_read.readline() #ignore first line
    count = int(content)
    i = 1
    while (content != ""  and i <= count):
        content = fd_read.readline()
        numbers = re.findall(r'\w+', content)
        if not numbers:
            break
        print "Calulating for result_set :"+str(i)
        fd_write.write ("Case #"+str(i)+": ")
        A = int(numbers[0])
        B = int(numbers[1])
        
        num_of_recycle = get_num_recycle(A, B)
        fd_write.write(str(num_of_recycle)+"\n")
        i +=1