file = open('input.txt','r')
strings = file.readlines()
file.close()

for i in range(0, len(strings)):
    strings[i] = strings[i].strip();

    
noOfTestCases = int(strings[0]);

file = open('output.txt','w');

index1 = 0;

for i in range(0, noOfTestCases):    
    index = i+1; 
    part = [];
    part =  [float(s) for s in strings[index].split()];

    c = float(part[0]);
    f = float(part[1]);
    x = float(part[2]);

    time = 0.0;
    totalf = 2.0;

    while ( (x / totalf) > ( (c / totalf) + (x/(totalf+f)) )):
        time  = time + (c / totalf);
        totalf = totalf + f;
        

    time  = time + (x/totalf);
    file.write("Case #"+str(index)+": "+str(format(time, '.7f'))+"\n");


    

file.close();        

