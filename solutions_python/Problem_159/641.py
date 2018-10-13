def min_needed(list1):
    max_diff = 0
    total_diff = 0
    sum = 0
    
    for i in xrange(1, len(list1)):
        diff = list1[i - 1] - list1[i]
        if diff > 0:
            total_diff += diff
            if diff > max_diff:
                max_diff = diff
            
    for i in xrange(len(list1)):
        x = list1[i]
        
        if x < max_diff and i != len(list1) - 1:
            sum += x
        elif i != len(list1) - 1:
            sum += max_diff
    
        
    return total_diff, sum




# a = "32 26 22 22 67 51"
# a = [int(i) for i in a.strip().split()]
# b, c = min_needed(a)
# print "Case #%d: %d %d\n" % (0, b, c)
            

file_name = 'A-large.in'
out = open('A_large.out', 'w')
with open(file_name) as f:
    T = int(next(f))
    count = 0
    case = 1
    
    for line in f:
        if count % 2 == 1:
            a = [int(i) for i in line.strip().split()]
            b, c = min_needed(a)
            out.write("Case #%d: %d %d\n" % (case, b, c))
            # print "Case #%d: %d %d\n" % (case, b, c)
            case += 1
        count += 1
out.close()