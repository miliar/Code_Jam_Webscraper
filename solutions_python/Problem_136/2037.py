file = open('B-small-attempt0.in','r')
fileans = open('ansB.txt','w')

case_num = int(file.readline().replace('\n', ''))
for i in range(case_num):
    nums = file.readline().replace('\n', '').split()
    sec = 0
    increase = 2
    c = float(nums[0])
    f = float(nums[1])
    x = float(nums[2])
    max_sec = x/increase
    y = sec + (x/(increase+f)) + c/increase
    while (y < max_sec):
        max_sec = y
        sec += c/increase
        increase += f
        y = sec + (x/(increase+f)) + c/increase
        
    sec += x/ increase
    fileans.write("Case #%s: %s\n" % (i+1,round(sec,7)))

file.close()
fileans.close()
print('DONE')