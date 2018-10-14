import operator
f = open("B-small-attempt2.in", "r")
g = open("output.txt","w")
number = int(f.readline())
for i in range(number):
    s = f.readline()
    s = s.split()
    n  = int(s[0])
    dic = {}

    dic["r"] = int(s[1])
    dic["o"] = int(s[2])
    dic["y"] = int(s[3])
    dic["g"] = int(s[4])
    dic["b"] = int(s[5])
    dic["v"] = int(s[6])
    # q1 = dic["r"]
    # q2 = dic["y"]
    # q3 = dic["b"]
    threshold = n/2
    main = max(dic.iteritems(), key=operator.itemgetter(1))[0]
    if dic[main] > threshold:
        g.write("Case #" + str(i + 1)+": IMPOSSIBLE\n")
    else:
        myset = set(["r","b","y"])
        myset.remove(main)
        myset = list(myset)
        sub1 = myset[0]
        sub2 = myset[1]

        triple = dic[sub1]+dic[sub2]-dic[main]
        if triple>0:
            ans = (main.upper()+sub1.upper()+sub2.upper())*triple
        else:
            ans = ""
        for j in "r","y","b":
            dic[j] -= triple
        while(dic[sub1] > 0 or dic[sub2]>0):
            dic[main] -= 1
            ans += main.upper()
            if dic[sub1]>0:
                dic[sub1] -= 1
                ans += sub1.upper()
            else:
                dic[sub2] -= 1
                ans += sub2.upper()
        # count1 = 0
        # count2 = 0
        # count3 = 0
        # for k in range(n):
        #     if k>= 1 and ans[k] == ans[k-1]:
        #         print(i)
        #     if ans[k] == "R":
        #         count1 += 1
        #     elif ans[k] == "Y":
        #         count2 += 1
        #     else:
        #         count3 += 1
        #
        # if count1 != q1 or count2 != q2 or count3 != q3:
        #     print(i)
        # if ans[0] == ans[-1]:
        #     print(i)
        g.write("Case #" + str(i + 1)+": "+ ans+ "\n")





