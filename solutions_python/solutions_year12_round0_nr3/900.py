'''
Created on Apr 14, 2012

@author: Vimuth
'''
inputfile = open('C-small-attempt0.in','r')
line = int(inputfile.readline());

def countRecycles(A,B):
    count = 0
    for i in range(A,B+1):
        for j in range(1,len(str(i))):
            recycled = int(str(i)[-j:]+str(i)[:-j]);
            if recycled in range(A,B+1) and recycled!=i and len(str(recycled))==len(str(i)):
                count+=1 
    return count/2
    
outputfile = open('output.out','w');


for i in range(0,line):
    text = inputfile.readline().split(' ');
    x = countRecycles(int(text[0]),int(text[1]))
    l = "Case #"+str(i+1)+": "+str(x)+"\n";
    print l
    outputfile.writelines(l);
    