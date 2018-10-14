import math

def fairAndSquare(filePath):
    file=open(filePath,"r");
    #result=open("outputFairAndSquare_large.txt","a");
    result=open("outputFairAndSquare_small_input.txt","a");
    data=file.readline().strip("\n");
    noOfTC=int(data);

    for x in range(0,noOfTC):
        noOfFairAndSquare=0;
        sentence=file.readline().strip("\n");
        numberList=sentence.split(" ");
        length=len(numberList);
        for y in range (int(numberList[0]),int(numberList[1])+1):
            #print(y);
            if(checkPalindrome(y)):
                root=math.sqrt(y);
                #print("Square Root: "+str(root));
                roundUp=int(root);
                if((root-roundUp)==0):
                    #print("Rounded Root: "+str(roundUp));
                    if(checkPalindrome(roundUp)):
                        noOfFairAndSquare=noOfFairAndSquare+1;
        print("Case #"+str(x+1)+": "+str(noOfFairAndSquare));
        result.write("Case #"+str(x+1)+": "+str(noOfFairAndSquare)+"\n");

    file.close();
    result.close();

def checkPalindrome(num):
    lst=[x for x in str(num)];
    tempLst=[x for x in str(num)];
    lst.reverse();
    if (lst==tempLst):
        return True;
    else:
        return False;



fairAndSquare("C:\\GoogleCodeJam\\2013\\FairAndSquare\\C-small-attempt0.in");
