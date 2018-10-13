t=int(input())
nums=[int(input()) for _ in range(t)]

for i in range(len(nums)):
    if nums[i]<10:
        print("Case #%d: %d"%(i+1,nums[i]))
        continue

    last=-1
    for j in range(nums[i],0,-1):
        digits=list(map(int,str(j)))
        tidy=True
        for k in range(len(digits)-1):
            if int(digits[k])>int(digits[k+1]):
                tidy=False
                break
        if tidy:
            last=j
            break

    print("Case #%d: %d"%(i+1,last))
