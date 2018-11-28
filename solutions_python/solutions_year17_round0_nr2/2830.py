#!/usr/bin/python
import pdb
case = 'B'

def func(datum):
    string = list(datum)[:-1]
    if len(string)==1:
        return "".join(string)
    for i in range(len(string), 1, -1):
        if string[i-1]<string[i-2]:
            if string[i-2]>1:
#                print "".join(string)
                string[i-2]=str(int(string[i-2])-1)
            change_the_rest_to_9ish(i-1, string)
    while True:
        if string[0]=='0':
            del string[0]
        else:
            break
    return "".join(string)

def change_the_rest_to_9ish(p, string):
#    print 'before', "".join(string)
    for i in range(p, len(string)):
        string[i] = '9'
#    print 'after ' ,"".join(string)
    return

def get(file_handler, row_per_case=1):
    result = []
    if row_per_case==1:
        return file_handler.readline()
    for i in range(0, row_per_case):
        result.append(file_handler.readline())
    return result


f = open('/tmp/'+case+'.in', 'r')
n = int(f.readline())
file_output = open('/tmp/'+case+'.out', 'w')
for i in range(0,n):
    datum = get(file_handler=f)
    result = func(datum)
    output = 'Case #'+str(i+1)+": "+str(result)
    print output
    file_output.write(output+'\n')

