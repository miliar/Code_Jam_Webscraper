#!/bin/python
input_file=open("C-small-attempt0.in","r")
output_file=open("C-small-attempt0.out","w")
lines=input_file.readlines()
for iline in range(0,len(lines)):
    dict_pair={}
    if iline==0:
        continue
    numbers=lines[iline].split()
    min=int(numbers[0])
    max=int(numbers[1])
    n_count=0
    for number in range(min, max):
        string=str(number)
        for ichar in range(0,len(string)-1):
            new_string=string[ichar+1:len(string)] + string[0:ichar+1]
            if new_string[0]!='0' and int(string)<int(new_string) and int(new_string)<=max and int(new_string)>min:
                n_count=n_count+1
                if [string,new_string] not in dict_pair.keys():
                    dict_pair[string,new_string]=''
#    print dict_pair
    output_file.write("Case #%d: %d\n" % (iline, len(dict_pair.keys())))
