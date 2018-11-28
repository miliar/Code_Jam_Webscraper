'''
Created on 10-May-2014

@author: vibhore
'''
# reverse words
# 2010 qual prob.No. b

from sys import stdout

# ip_file = r'..\jam\input.in'
# op_file = r'..\jam\task.out'

ip_file = r'..\..\..\jam\input.in'
op_file = r'..\..\..\jam\task1.out'
#MODE = 'debug'
MODE = 'run'
#MODE = 'test'

def myprint(*args):
    if MODE== 'debug':
        print args

class read_ip:
 
    def __init__(self, file_name):
        self.line_no = 0
        f = open(file_name, 'r')
        self.lines = f.readlines()
        f.close()
        myprint ('read lines,123,: ', self.lines)
    
    def get_lines(self):
        return self.lines

    def next_line(self):
        l = self.lines[self.line_no]
        self.line_no += 1
        return l
        
    def next_int(self):
        n = int(self.lines[self.line_no].strip())
        self.line_no += 1
        return n 

    def next_int_array(self):
        tmp = self.lines[self.line_no].split()
        self.line_no += 1
        nos = [int(i) for i in tmp]
        return nos

    def next_word(self):
        '''will return character or word in the next line
        #note: BEWARE, if next line contains multiple words it will meerge all of them
        '''
        n = self.lines[self.line_no].strip()
        self.line_no += 1
        return n

    def next_word_array(self):
        words = self.lines[self.line_no].split()
        self.line_no += 1
        return words


class write_op():
    def __init__(self, file_name):
        self.opf = open(file_name,'w')   
       
    def myprint(self, txt):
        if MODE == 'debug':
            stdout.write(txt)
        if MODE == 'run':
            self.opf.write(txt)
        if MODE == 'test':
            stdout.write(txt)
            self.opf.write(txt)
            
    def close(self):
        self.opf.close()
    
    def get_fp(self):
        return self.opf
        
def solve(r, w,tc):
    f = r.next_line()
    f = f.strip()
    myprint(f)
    p,q = f.split('/')
    P= int(p)
    Q= int(q)
    for n in range(0,19+1):
        if 1<<n & Q != 0:
            break
    ndeno =n
    myprint('ndeno:', ndeno)
    factor= Q/ (1<<ndeno)
    myprint('fac:',factor )
    if P%factor !=0: 
        w.myprint('Case #'+str(tc)+': impossible\n')
    else: 
        P=P/factor; 
        #To find leftmost 1 in P 
        for n in range(19,-1,-1) : 
            if (1<<n)&P != 0 :
                break;      
        nnum=n 
        y= ndeno-nnum
        w.myprint('Case #'+str(tc)+': '+str(y)+'\n') 
         
    
if __name__ == "__main__":    
    r = read_ip(ip_file)
    w = write_op(op_file)
    t = r.next_int()
    for tc in range(1, t + 1):
        solve(r, w,tc)

        