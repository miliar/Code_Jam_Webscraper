f = open('C:/Users/Asis/Downloads/ggg.in', 'r')
#f = open('G:/Study/Code Jam/trial.txt', 'r')
g = open('G:/Study/Code Jam/output4_2.txt', 'w')
no_test_cases = int(f.readline())
for i in range(1,no_test_cases+1):
    nums_str = f.readline()
    nums = nums_str.split()
    for l in range(len(nums)):
        nums[l] = int(nums[l])
    N = nums[0]
    S = nums[1]
    p = nums[2]
    totals = []
    for k in range(3,len(nums)):
        totals.append(nums[k])
    totals.sort()
    totals.reverse()
    poss = 0
    for k in range(N):
        if p == 0:
            poss += 1
        elif totals[k] >= 3*(p-1)+1:
            poss += 1
        elif (S > 0) and ((totals[k] == (3*(p-1))) or (totals[k] == (3*(p-1)-1))) and totals[k] != 0:
            S -= 1
            poss += 1
    g.write("Case #"+str(i)+": "+str(poss)+chr(10))
g.close()
f.close()
