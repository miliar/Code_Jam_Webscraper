fp = open('output.txt','w+')
t = int(raw_input());

for case in range(1,t+1):
    ip = raw_input().split(' ');
    string = ip[0];
    n = int(ip[1]);
    ans = 0;
    for i in range(len(string)):
        count = 0;
        flag = 0;
        for j in range(i,len(string)):
            c = string[j];
            if(c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u'):
                count += 1;
                if(count >= n):
                    flag = 1;
                    ans += 1;
            elif(flag == 0):
                count = 0;
            elif(flag == 1):
                ans += 1;
    fp.write("Case #" + str(case) + ": " + str(ans) +"\n");
    t -= 1;
