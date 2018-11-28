import re;

f = open ( 'A-large.in' , 'r');

tmp = f.readline();
tmp =tmp.split()
a = int(tmp[0]);
b = int(tmp[1]);
c = int(tmp[2]);

dic = [];

for i in range(b):
    dic.append(f.readline());

patterns = [];

def reginator(n):
    result = ''
    
    for c in n:
        if c == '(':
            result += '['
        elif c == ')':
            result += ']'
        else:
            result += c

    return result


for  d in f:
    patterns.append(reginator(d))

j = 1;

w = open ( 'Output.txt' , 'w');

for a in patterns:
    reg = re.compile( a );
    i = 0;
    for b in dic:
        if re.match ( reg , b ):
            i = i+1;
    print ('Case #' + str(j) + ': ' + str(i) )
    w.write('Case #' + str(j) + ': ' + str(i)+ '\n')
    j += 1


