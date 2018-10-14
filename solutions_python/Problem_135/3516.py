in1 = open ("p1.in", "r")
testCases = int(in1.readline());
for x in range (1, testCases+1):
    counter=0;
    guess = int(in1.readline());
    for y in range (1,5):
        str1=in1.readline();
        if (y == guess):
            nums1 = str1.split();
    guess = int(in1.readline());
    for z in range (1,5):
        str1=in1.readline();
        if (z == guess):
            nums2 = str1.split();
            for i in range (0,4):
                for j in range (0,4):
                    if (nums2[i] == nums1[j]):
                        counter+=1;
                        answer = nums2[i];
    if (counter == 0):
        print ("Case #"+str(x)+": Volunteer cheated!");
    elif (counter ==1):
        print ("Case #"+str(x)+": "+answer);
    else:
        print ("Case #"+str(x)+": Bad magician!");
