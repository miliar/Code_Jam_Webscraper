def solve():
    f=open("B-small-attempt1.in")
    f2=open("output.txt",'w')
    lines=f.readlines()
    t=int(lines[0])
    # t=input()
    for test in xrange(1,t+1):
        num=lines[test][:-1]
        # num=raw_input()
        ans=num
        num=list(num)
        i,tidy=0,True
        for x in xrange(len(num)-1):
            if num[x+1]>num[x]:
                i+=1
            elif num[x+1]<num[x]:
                tidy=False
                break

        if not tidy:
            if num[i]=='1':
                ans="9"*(len(num)-1)
            else:
                ans="".join(num[:i])+chr(ord(num[i])-1)+"9"*(len(num)-i-1)
        # print ans
        f2.write("Case #{}: {}\n".format(test,ans))
    f2.close()
    f.close()
solve()
