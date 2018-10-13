import sys;

numCases = int(input());
#sys.stdin.readline().split();

#numCases = int(t[0]);
nines = "999999999999999999";

for i in range(numCases):

    s = input().split(" ");
    n = s[0];
    nlen = len(n);
    
    lastInc = 0;
    output = "Case #{}: {}".format(i+1, n);
    
    
    #
    for j in range(1,nlen):
        if (n[j-1] < n[j]):
            lastInc = j;
            #print("lastInc {}".format(lastInc));
        else:
            if (n[j-1] > n[j]):
                if (lastInc == 0):
                    val = int(n[0]) - 1;
                    num9 = nlen - 1;
                else:
                    val = int(n[:lastInc+1]) -1;
                    #print(val);
                    num9 = nlen - lastInc -1;
                if (val == 0):
                    output = "Case #{}: {}".format(i+1, nines[:num9]);
                else:
                    output = "Case #{}: {}{}".format(i+1, val, nines[:num9]);
                break;
    print(output);
    

