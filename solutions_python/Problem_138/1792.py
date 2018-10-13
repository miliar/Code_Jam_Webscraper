file = open('input.txt','r')
strings = file.readlines()
file.close()

for i in range(0, len(strings)):
    strings[i] = strings[i].strip();

    
noOfTestCases = int(strings[0]);

file = open('output.txt','w');

index = 0;

for j in range(0, noOfTestCases):    
    index = 1 + (j*3);
    score1 = 0;
    score2 = 0;
    noOfWeights = 0;

    noOfWeights = int(strings[index]);

    weights1 =  [float(s) for s in strings[index+1].split()];
    weights2 =  [float(s) for s in strings[index+2].split()];

    weights1.sort();
    weights2.sort();

    while len(weights1) > 0:
        if len(weights1) == 1:
            if(weights1[0] > weights2[0]):
                score1 = score1 + 1;
               
            weights1.remove(weights1[0]);
            weights2.remove(weights2[0]);        
        else:
            for i in weights1:            
                if i > min(weights2):
                        score1 = score1 + 1;
                        break;

            weights1.remove(i);
            weights2.remove(min(weights2));



    weights1 =  [float(s) for s in strings[index+1].split()];
    weights2 =  [float(s) for s in strings[index+2].split()];

    weights1.sort();
    weights2.sort();

    while len(weights1) > 0:
        if len(weights1) == 1:
            if(weights1[0] > weights2[0]):
                score2 = score2 + 1;
               
            weights1.remove(weights1[0]);
            weights2.remove(weights2[0]);        
        else:
            check = 0;
            for i in weights2:
                check = check + 1;
                if i > min(weights1):
                    break;
                if check == len(weights2):
                    score2 = score2 + 1;
                    check = -1;

            weights1.remove(min(weights1));
            if(check == -1):
                weights2.remove(min(weights2));
            else:
                weights2.remove(i);

    file.write("Case #"+str(j+1)+": "+str(score1)+" "+str(score2)+"\n");


    

file.close();        



