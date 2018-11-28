def increasing(n):
    last = 0
    lst = list(str(n))
    for index, x in enumerate(lst):
        if int(x) >= last:
            last = int(x)
            continue
        else:
            num = int(''.join(lst[0:index])) - 1
            return increasing(int(str(num) + '9'*len(lst[index:])))
    
    return int(n)
        
f_r = open('C:/Users/anton/Documents/CodeJam/B-large.in', 'r')
f_w = open('answer_large.out', 'w')

t = int(f_r.readline())
nums = [int(x) for x in f_r]
f_r.close()

for index, z in enumerate(nums):
    f_w.write("Case #" + str(index+1) + ': ' + str(increasing(z)) + "\n")

f_w.close()