in_file = open('tidy_nums.in')
cases = int(in_file.readline().strip())
results = []

for case in range(cases):
    num = '0'+in_file.readline().strip()
    index = 1
    while index < len(num):
        if num[index]<num[index-1]:
            num = num[:index-1]+str(int(num[index-1])-1)+'9'*(len(num)-index)
            index = index-1
        else:
            index+=1
    results.append("Case #{}: {}".format(case+1,int(num)))
in_file.close    

out_file = open('tidy_nums.out','w')
    
for result in results:
    print(result)
    out_file.write(result+'\n')

out_file.close