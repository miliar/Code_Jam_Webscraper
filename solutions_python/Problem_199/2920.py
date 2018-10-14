import sys;

numCases = int(input());
#sys.stdin.readline().split();

#numCases = int(t[0]);

for i in range(numCases):

    s = input().split(" ");
    pancakes = s[0];
    k = int(s[1]);
    #= sys.stdin.readline().split();
    numFlips = 0;
    
    #print(pancakes);
    for x in range(len(pancakes) + 1 - k):

        if pancakes[x] == '-':
            pancakes = pancakes[:x] + '+' + pancakes[x+1:];
            #print(pancakes);
            numFlips = numFlips+1;
            for j in range(1,k):
                if pancakes[x+j] == '-':
                    #print("C");
                    pancakes = pancakes[:x+j] + '+' + pancakes[x+j+1:];
                    #print(pancakes);
                else:
                    #print("D");
                    pancakes = pancakes[:x+j] + '-' + pancakes[x+j+1:];
        #print(pancakes);

    slen = len(pancakes);
    for j in range(1,k):
        if pancakes[slen-j] == '-':
            numFlips = -1;
    
    if numFlips == -1:
        print("Case #{}: IMPOSSIBLE".format(i+1));
    else:
        print("Case #{}: {}".format(i+1, numFlips));
    

