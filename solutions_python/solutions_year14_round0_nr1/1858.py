file = open('input.txt','r')
strings = file.readlines()
file.close()

for i in range(0, len(strings)):
    strings[i] = strings[i].strip();

    
noOfTestCases = int(strings[0]);

file = open('output.txt','w');

for i in range(0, noOfTestCases):
    ansRow1 = 0;
    ansRow2 = 0;
    index1 = 0;
    index2 = 0 ;

    index1 = 1+(i*10);
    index2 = 6+(i*10);

    ansRow1 = int( strings[index1] );
    ansRow2 = int( strings[index2] );

    part1 = [];
    part2 = [];

    part1 =  [int(s) for s in strings[index1 + ansRow1].split() if s.isdigit()];

    part2 =  [int(s) for s in strings[index2 + ansRow2].split() if s.isdigit()];
   
    check1 = set(part1);
    check2 = set(part2);

    check2.intersection_update(check1);

    if len(check2) == 1:
        for j in range(1,17):
            if j in check2:
                 file.write("Case #"+str(i+1)+": "+str(j)+"\n");
    elif len(check2) > 1:
        file.write("Case #"+str(i+1)+": Bad magician!\n");
    elif len(check2) == 0:
        file.write("Case #"+str(i+1)+": Volunteer cheated!\n");


file.close();        
