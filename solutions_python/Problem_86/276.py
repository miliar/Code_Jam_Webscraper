is_harmonious = lambda l: lambda n: reduce(lambda a,b: a and b ,[n % i == 0 or i % n == 0 for i in l])
file = open(r'C:\PyProj\Test\C-small-attempt6.in')
out = open(r'C:\PyProj\Test\C-small-attempt6.txt','w')
test_count = int(file.readline())

result_set = []

for t in range(1,test_count+1):
    line_1 = [int(s) for s in file.readline().split()]
    line_2 = [int(s) for s in file.readline().split()]
    other_guys = line_1[0]
    range_start = line_1[1]
    range_end = line_1[2]
    test = is_harmonious(line_2)
    result = [i for i in range(range_start,range_end+1) if test(i)]    
    if len(result) > 0:
        result.sort()
        result_set.append('Case #' + str(t) +': ' + str(result[0]))
    else:
        result_set.append('Case #'+ str(t) +': NO')
    
for r in result_set:
    out.write(r +'\n')