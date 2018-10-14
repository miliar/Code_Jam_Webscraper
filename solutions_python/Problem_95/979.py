import re

inputfile = open('A-small-attempt2.in','r')
line = int(inputfile.readline());
mappings = {}

strings = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv']
translations = ['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up']

for i in range(0,3):
    for j in range(0,len(strings[i])):
        if(strings[i][j]!=' '):
            mappings[strings[i][j]]=translations[i][j]

mappings['z'] = 'q';
mappings['q'] = 'z';
mappings[' '] = ' ';

def translate(input):
    temp = list()
    for i in range(0,len(input)):
        if mappings.has_key(input[i]):
            temp.append(mappings[input[i]])
    return ''.join(temp) 

outputfile = open('output.out','w');


for i in range(0,line):
    text = inputfile.readline();
    temp = translate(text)
    print temp
    l = "Case #"+str(i+1)+": "+temp+"\n";
    outputfile.writelines(l);
    