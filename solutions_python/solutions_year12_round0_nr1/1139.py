'''
Created on Apr 14, 2012

@author: ashishgaunkar
'''

mapping = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v',
           'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b',
            'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j',
            'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'
            
            }

import re

input_path = '/Users/ashishgaunkar/zmqworkspace/Test/A-small-attempt1.in'
output_path = '/Users/ashishgaunkar/zmqworkspace/Test/A-small-attempt1.op'
    
    
def convert(word):
    '''
    This method wil return the word coverted
    '''
    ret = ''
    for w in word:
        ret += mapping.get(w, w)
    return ret+' '
    
if __name__ == '__main__':

    fd_read = open(input_path)
    fd_write = open(output_path, 'w')
    #fd_write.write("Output\n")
    
    content = fd_read.readline() #ignore first line
    count = int(content)
    i = 1
    while (content != ""  and i <= count):
        content = fd_read.readline()
        words = re.findall(r'\w+', content)
        if not words:
            break
        print "Writing line number :"+str(i)
        fd_write.write ("Case #"+str(i)+": ")
        for word in words:
            fd_write.write(convert(word))
        fd_write.write("\n")
        i +=1
        

        
    

#        line = read_next_line(f)