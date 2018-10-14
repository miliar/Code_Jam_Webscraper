global flipcounter

def flip(line,start,k):
    global flipcounter
    for t in range(k):
        if(line[start + t]) == '+':
            line[start + t] = '-'
        else:
            line[start + t] = '+'
    flipcounter= flipcounter +1
    
def myfunc(line,k):
    global flipcounter
    
    flipcounter = 0;
    
    pluscounter =0
    for i in range(len(line)-k+1):
        if(line[i] == '+'):
            pluscounter = pluscounter + 1
            continue
        else:
            flip(line,i,k)
            
    if(pluscounter == len(line)):
        return

    pluscounter =0;
    for i in range(len(line)):
        if(line[i] == '+'):
            pluscounter = pluscounter + 1
    if(pluscounter == len(line)):
        return
    
    
    line = list(reversed(line))
    
    for i in range(len(line)-k+1):

        if(line[i] == '+'):
            pluscounter = pluscounter + 1
            continue
        else:
            flip(line,i,k)
            
    return "impossible"

myfile = open("A-large.in", "r") 
noofcases = myfile.readline();
outfile = open("outputlarge", 'w')
for i in range(int(noofcases)):
    myinput = myfile.readline();
    mylist = myinput.split( );
    returnval = myfunc (list(mylist[0]),int(mylist[1]),)
    if(returnval == "impossible"):
        outfile.write("Case #" + str(i+1) + ": IMPOSSIBLE\n" )  # python will convert \n to os.linesep
    else:
        outfile.write("Case #" + str(i+1) + ": " + str(flipcounter)+"\n" )  # python will convert \n to os.linesep

outfile.close()
