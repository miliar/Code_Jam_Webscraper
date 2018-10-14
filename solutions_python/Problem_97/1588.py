import sys

file = open(sys.argv[1], 'r')
t = int(file.readline())

for testcase in range (1,t+1) :
    nm = file.readline();
    n = int(nm.split(' ')[0]);
    m = int(nm.split(' ')[1]);
    digits = len(str(m));
    ans = 0;
    for num in range(n,m+1) :
        doublenum = str(num)+str(num);
        for k in range(1,digits+1) :
            if(int(num) < int(doublenum[k:k+digits]) and int(doublenum[k:k+digits]) <= int(m)) :
                ans = ans+1;
#                print str(num)+" is less than "+doublenum[k:k+digits]

    print "Case #"+str(testcase)+ ": "+str(ans);

