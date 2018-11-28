import sys
sys.setrecursionlimit(10000)
f= open("input.txt",'r');
out = open('out.txt','w');

orig_stdout = sys.stdout

sys.stdout = out

T = int(f.readline());

def takeinput():
    global f;
    a=[];
    finput = f.readline().rstrip();
    a = [ float(n) for n in finput.split(" ")];
    return a;

C=0;
F=0;
X=0;
val="";
def compute(rate,time):
    global C,F,X,val;
    
    #if not buying farm time taken to reach X
    tX = X/rate;
    #else if buying a farm and then villa
    tF= (C/rate);

    #and the villa
    tXF  = tF + (X/(rate+F));
    
    if(tX < tXF):
        #print "time is "+str(time + tX);
        val = str(time + tX);
        return time + tX;
    else:
        compute(rate+F,time + tF)
        
    
    
    

for i in range(0,T):
    #print takeinput();
    a= takeinput();
    C = a[0];
    F = a[1];
    X = a[2];
    compute(2,0);
    print("Case #"+str(i+1)+": "+val)
        
sys.stdout = orig_stdout
f.close();
out.close();


    
