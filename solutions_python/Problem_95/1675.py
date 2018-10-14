'''
Created on 14.04.2012

@author: Marco
'''

def read_file(adress):
    read_index = []
    f = open(adress, 'r')
    for line in f:
        read_index.append(line)
    f.close()
    # Deletes the line breaks '\n'.
    index = []
    for entry in read_index[1:]:
        if '\n' in entry:
            index.append(entry[:len(entry)-1])
        else:
            index.append(entry[:len(entry)])
    return index

def write_file(return_list, adress):
    case = 1
    f = open(adress, 'w')
    for line in return_list:
        write_line = 'Case #'+ str(case)+': '+line+'\n'
        f.write(write_line)
        case = case + 1
    f.close()

def change_strings(read_list): 
    write_list = []   
    for line in read_list:
        new_line = ''
        for char in line:
            if char == ' ':
                new_line = new_line + ' '
            elif char == 'a':
                new_line = new_line + 'y'    
            elif char == 'b':
                new_line = new_line + 'h'
            elif char == 'c':
                new_line = new_line + 'e'    
            elif char == 'd':
                new_line = new_line + 's'    
            elif char == 'e':
                new_line = new_line + 'o'
            elif char == 'f':
                new_line = new_line + 'c'    
            elif char == 'g':
                new_line = new_line + 'v'    
            elif char == 'h':
                new_line = new_line + 'x'    
            elif char == 'i':
                new_line = new_line + 'd'    
            elif char == 'j':
                new_line = new_line + 'u'
            elif char == 'k':
                new_line = new_line + 'i'
            elif char == 'l':
                new_line = new_line + 'g'    
            elif char == 'm':
                new_line = new_line + 'l'    
            elif char == 'n':
                new_line = new_line + 'b'    
            elif char == 'o':
                new_line = new_line + 'k'    
            elif char == 'p':
                new_line = new_line + 'r'    
            elif char == 'q':
                new_line = new_line + 'z'
            elif char == 'r':
                new_line = new_line + 't'    
            elif char == 's':
                new_line = new_line + 'n'
            elif char == 't':
                new_line = new_line + 'w'
            elif char == 'u':
                new_line = new_line + 'j'    
            elif char == 'v':
                new_line = new_line + 'p'    
            elif char == 'w':
                new_line = new_line + 'f'    
            elif char == 'x':
                new_line = new_line + 'm'    
            elif char == 'y':
                new_line = new_line + 'a'    
            elif char == 'z':
                new_line = new_line + 'q'
        write_list.append(new_line)
    return write_list

read_list = read_file('C:/Users/Marco/Desktop/A-small-attempt0.in')
return_list = change_strings(read_list)
write_file(return_list, 'C:/Users/Marco/Desktop/A-small-attempt0.out')

                       
#Input
#3
#ejp mysljylc kd kxveddknmc re jsicpdrysi
#rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#de kr kd eoya kw aej tysr re ujdr lkgc jv
#
#
#Output
#Case #1: our language is impossible to understand
#Case #2: there are twenty six factorial possibilities
#Case #3: so it is okay if you want to just give up