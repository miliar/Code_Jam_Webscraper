def findDigits(s):
    testS = s;
    ans0 = "";
    ans1 = "";
    ans2 = "";
    ans3 = "";
    ans = "";
    c = testS.count("Z")
    ans0 = ans0 + "0" * c;
    testS = testS.replace("O","",c);    #
    c = testS.count("W")
    ans2 = ans2 + "2" * c;
    testS = testS.replace("T","",c);
    testS = testS.replace("O","",c);
    c = testS.count("U")
    ans = ans + "4" * c;
    testS = testS.replace("F","",c);
    testS = testS.replace("O","",c);
    c = testS.count("F")
    ans = ans + "5" * c;
    testS = testS.replace("I","",c);
    testS = testS.replace("V","",c);
    c = testS.count("X")
    ans = ans + "6" * c;
    testS = testS.replace("I","",c);    #
    c = testS.count("V")
    ans = ans + "7" * c;
    c = testS.count("G")
    ans = ans + "8" * c;
    testS = testS.replace("I","",c);    #  
    testS = testS.replace("T","",c);
    c = testS.count("I");
    ans = ans + "9" * c;
    c = testS.count("O");
    ans1 = ans1 + "1" * c;
    c = testS.count("T")
    ans3 = ans3 + "3" * c;
    
    return ans0 + ans1 + ans2 + ans3 + ans;

t = int(input());
for i in range(1, t + 1):
    origStr = input();
    ans = findDigits(origStr);
    print("Case #{}: {}".format(i, ans));