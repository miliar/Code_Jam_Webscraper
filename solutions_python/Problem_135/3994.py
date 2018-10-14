filename = input();
testfile = open(filename);
outputfile = open("output.txt", "w");
num_test_cases = int(testfile.readline().replace("\n",""));
testcase = 1;
while(testcase<=num_test_cases):
    first_answer = int(testfile.readline().replace("\n",""));
    cards = [];
    for i in range(0, 4):
        cards.append(testfile.readline().replace("\n","").split());
    first_row = cards[first_answer-1];
    second_answer = int(testfile.readline().replace("\n",""));
    cards2 = [];
    for i in range(0, 4):
        cards2.append(testfile.readline().replace("\n","").split());
    second_row = cards2[second_answer-1];
    answer=0;
    count=0;
    for i in first_row:
        for j in second_row:
            if(i==j):
                answer = i;
                count+=1;
    if(answer!=0 and count==1):
        outputfile.write(("Case #"+str(testcase)+": "+answer+"\n"));
    elif(answer!=0 and count>1):
        outputfile.write(("Case #"+str(testcase)+": Bad magician!\n"));
    else:
        outputfile.write(("Case #"+str(testcase)+": Volunteer cheated!\n"));
    testcase+=1;
testfile.close();