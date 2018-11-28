c = int(raw_input())
for c in range(1,c+1):
    ans=0
    nums = map(int,raw_input().split())
    dancers = nums[0]
    surprising = nums[1]
    goal = nums[2]
    for i in range(3,len(nums)):
        score = nums[i]
        if score/3>=goal:
            ans+=1
            continue
        if score/3==goal-1 and score%3>0:
            ans+=1
            continue
        if surprising>0 and score>1:
            if score%3==0 and score/3==goal-1:
                surprising-=1
                ans+=1
            elif score%3==2 and score/3==goal-2:
                surprising-=1
                ans+=1
    print "Case #"+str(c)+": " + str(ans)
