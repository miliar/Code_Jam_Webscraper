test = int(input())
answer = []

for a in range(test):
    nums = input().strip().split()
    x = int(nums[0])
    r = int(nums[1])
    c = int(nums[2])

    ans = True
    s = r*c
    if x == 1:
       final = "Case #" + str(a+1) + ": GABRIEL"
       answer.append(final)
       continue
    
    if x>6:
        ans = False
    
    if (x*2) > s:
        ans = False

    if ((r < x) and (c < x)):
        ans = False
    if x == 2:
        if (s%x) == 0:
            final = "Case #" + str(a+1) + ": GABRIEL"
            answer.append(final)
            continue
        
    if (s%x) != 0:
        ans = False
        
    if x == 3:
        if (r == 1) or (c == 1):
            ans = False

    if (x == 4) or (x == 5):
        if (r < 3) or (c < 3):
            ans = False
        
    if ans:
        final = "Case #" + str(a+1) + ": GABRIEL"
    else:
        final = "Case #" + str(a+1) + ": RICHARD"

    answer.append(final)
    
for i in answer:
    print(i)
    
