def doProb(fname, ofname):
    #do problem 1 given a file name
    f = open(fname, 'r');
    nlines = int(f.readline());
    output = ['Case #' + str(i) + ': '+ getstate([int(j) for j in f.readline().split()]) + '\n' for i in range(1,nlines+1)];
    f.close();  
    of = open(ofname, 'w');
    of.writelines(output);
    of.close();

def getstate(v):
    #get the state of a light bulb for n flippers after k flips
    if((v[1]+1)%(2**v[0])==0):
        return "ON";
    else:
        return "OFF";

