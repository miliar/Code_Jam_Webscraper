inputData = [];
infile = open("B-large.in","r");
line = infile.readline();
TestCases = int(line);
line = infile.readline();
testCase = 0;
while line!="":
    fields = line.split();
    people = int(fields[0]);
    surprises = int(fields[1]);
    threshold = int(fields[2]);
    scores = []
    for index in  range(3,3+people):
        scores.append(int(fields[index]));
    inputData.append((people,surprises,threshold,scores));
    line = infile.readline();
    testCase+=1;
infile.close();


def getCountDancingG(people,surprises,threshold,data):
    individualData = {}
    count = 0;
    totalCountOfGooglers = 0
    for  i in range(people):
        quo,rem = divmod(data[i],3);
        individualData[i] = [quo,rem];
    greedyDataIndex = sorted(individualData,key= lambda a: individualData[a][0],reverse = True);
    for index in greedyDataIndex:
        if individualData[index][0] >= threshold:
            totalCountOfGooglers+=1;
        elif individualData[index][1] == 1:
            if (individualData[index][0]+1)>=threshold and (1+individualData[index][0])<=10:
                totalCountOfGooglers+=1;
        elif individualData[index][1] == 2 :
            if (1+individualData[index][0])>=threshold and (1+individualData[index][0])<=10:
                    totalCountOfGooglers+=1;
            elif (2+individualData[index][0])>=threshold and count<surprises and (2+individualData[index][0])<=10:
                    count+=1;
                    totalCountOfGooglers+=1;
        elif count < surprises and individualData[index][1] == 0:
            if individualData[index][0] >= 1 and (1+individualData[index][0])>=threshold and(1+individualData[index][0])<=10:
                count+=1;
                totalCountOfGooglers+=1;
    #assert (count<=surprises);
    return totalCountOfGooglers;

outfile = open("B-large2.txt","w");
for i in range(TestCases):
    print inputData[i][3];
    outfile.write("Case #%d: %d\n"%(i+1,getCountDancingG(inputData[i][0],inputData[i][1],inputData[i][2],inputData[i][3])));
outfile.close();
