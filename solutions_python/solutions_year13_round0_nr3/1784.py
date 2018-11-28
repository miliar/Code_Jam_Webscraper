from math import *;
def numberdigits(x):
    return len(str(x));

def ndigit(x, n):
    s = str(x);
    return s[numberdigits(x)-n];

def ispalindrome(x):
    if (x - int(x) != 0.0):
        return 0;
    x = int(x);
    result = 1;
    nd = numberdigits(x);
    for i in range(1,int(nd/2)+1):
        if (ndigit(x,nd+1-i) != ndigit(x,i)):
            result = 0;
    return result;

f = open("C-small-attempt0.in", "r")
text = f.readlines()
result = [];
for i in range(1,len(text)):
    result = result + [text[i].replace("\n","")];
f.close();
fo = open('myfile.txt','w')

for i in range(0,len(result)):
    count = 0;
    for j in range(int(result[i][0:result[i].find(" ")]),int(result[i][result[i].find(" ")+1:len(result[i])])+1):
        if(ispalindrome(j) and ispalindrome(sqrt(j))):
            count= count + 1;
    fo.write('Case #' + str(i+1) + ': ' + str(count) + '\n');    

fo.close();

print "Termine";
    
            
        

