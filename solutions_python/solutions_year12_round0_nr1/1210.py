#!/usr/bin/python
if __name__ == "__main__":  
    
    dict = {'a' : 'y',\
'b' : 'h',\
'c' : 'e',\
'd' : 's',\
'e' : 'o',\
'f' : 'c',\
'g' : 'v',\
'h' : 'x',\
'i' : 'd',\
'j' : 'u',\
'k' : 'i',\
'l' : 'g',\
'm' : 'l',\
'n' : 'b',\
'o' : 'k',\
'p' : 'r',\
'r' : 't',\
's' : 'n',\
't' : 'w',\
'u' : 'j',\
'v' : 'p',\
'w' : 'f',\
'x' : 'm',\
'y' : 'a',
'q' : 'z',
'z' : 'q'}
    f = open('A-small-attempt0.in', 'r')
    t = int(f.readline())
    for i in range(t):
        line = f.readline()
        x = []
        for j in range(len(line)-1):
            if line[j] != ' ':
                x.append(dict[line[j]])
            else:
                x.append(line[j])
        print "Case #"+str(i+1)+": "+("".join(x))
    '''
    f = open('training.txt', 'r')
    t = int(f.readline())
    dict = {}
    for i in range(t):
        init = f.readline()
        sol = f.readline()
        for poz in range(len(init)):
            if init[poz] != ' ' and init[poz] != '\n':
                dict[init[poz]] = sol[poz]
    sorted_list = [x for x in dict.iteritems()] 
    sorted_list.sort(key=lambda x: x[0]) 
    for key, val in sorted_list:
        print '\''+str(key)+'\' : \''+str(val)+'\',\\'

    '''
    f.close()
    