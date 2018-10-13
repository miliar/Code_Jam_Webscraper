# surprising if two apart
# more than two apart wille ver happen

# total:
#  sum of the three scores
# best:
#  maximum of teh three scores

# given total points, and number of surprising triplets,
    # max # who coudl have had max p?

# 29, 20, 8, 18, 18, 21
# 2 surprising triplets
# how many had max >= 8

dirt = r'C:\Users\JJ\Downloads\B-large.in'
#dirt = r'C:\GCJ\in.txt'

with open(dirt, 'r') as thefile:
    temp = thefile.read()
    temp = temp.split('\n')

temp.pop(0)
temp.pop(-1)
output = []
for line in temp:
    tmp = line.split(' ')
    nums = map(int,tmp)
    N = nums[0]
    S = nums[1]
    p = nums[2]
    totals = nums[3:]

    # now that it's read in, let's do this thing

    # if %3==0:
    #  18: 666 567 (2)
    # ==1: 19: 667 (1)
    # ==2: 20: 668 677 (2)
    
    # remember, not __future__ division! perfect

    # Ex:
    # looking for 8 or better
    # >=24, ignore b/c guaranteed
    # 23, 788
    # 22, 778
    # 21: first one that has no 8 in nonsurprising
    # 21: 678
    # 20: 668
    # 19: NO b/c can't do 568

    # so the question is (p-1)*3-1>x>(p-1)*3
    #   find max([S,x])
    #   answer is max(S,x) + num(>=(p-1)*3+1)

    answer = 0
    maybes = 0

    if p == 0:
        answer = len(totals)
    elif p == 1:
        answer = len([x for x in totals if x >= 1])
    else:
        for num in totals:
            if num >= (p-1)*3+1:
                #print('answer ' + str(num))
                answer += 1
            elif num in [(p-1)*3-1, (p-1)*3]:
                #print('maybes ' + str(num))
                maybes += 1
        #print(str(min([S, maybes])))
        answer += min([S, maybes])

    output.append(str(answer))


with open(r'C:\GCJ\out.txt', 'w') as outputfile:
    outputfile.write('\n'.join(
        ["Case #%s: %s" % (index+1, content) \
        for index, content in enumerate(output)]
        ))
    
