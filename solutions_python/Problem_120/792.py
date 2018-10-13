input_line = raw_input()
N = int(input_line)
input_list = []
for i in xrange(N):
    (start,end) = raw_input().split(' ')
    num1 = int(start)
    num2 = int(end)
    input_list.append([num1,num2])
result_dict = {}
ctr = 1
for inputs in input_list:
    r = inputs[0]
    t = inputs[1]
    outer = r+1
    inner = r
    outmininsq = outer**2 - inner**2
    rem_paint = t
    cnt = 0
    while outmininsq <= rem_paint:
        rem_paint -= outmininsq
        cnt += 1
        outer += 2
        inner += 2
        outmininsq = outer**2 - inner**2
        
    result_dict[ctr] = cnt
    ctr+=1
for key in result_dict:
    print "Case #"+str(key)+": "+str(result_dict[key])