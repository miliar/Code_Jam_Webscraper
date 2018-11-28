import sys

def get_items(indexarray, sarray):
    result = []
    for index in indexarray:
        result.append(sarray[index])
    return result

def adder(ops):
    length = len(ops)
    result = []
    for i in range(20):
        count = 0
        for j in range(length):
            if ops[j][i] == '1':
                count = count + 1
        if count % 2 == 0:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
    
def itobin(i):
    result = []
    tmp = i
    while tmp>0:
        result.append(str(tmp%2))
        tmp = tmp/2
    while len(result) < 20:
        result.append('0')
    result_str = ''.join(result)
    result = result_str[::-1]
    return result

def check_p(bin_cs):
    pos = True
    length = len(bin_cs)
    for i in range(20):
        count = 0;
        for j in range(length):
            if bin_cs[j][i] == '1':
                count = count+1
        if count%2 != 0:
            pos = False
            break;
    return pos

def combine_set(total, num):
    for i in xrange(len(total)):
        if num == 1:
            yield (total[i],)
        else:
            for next in combine_set(total[i+1:len(total)], num-1):
                yield (total[i],) + next

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename,'r')
    t = int(f.readline())
    
    for i in range(t):
        n = int(f.readline())
        candies = f.readline().split(' ')
        bin_cs = []
        for j in range(n):
            bin_cs.append(itobin(int(candies[j])))
        
        if not check_p(bin_cs):
            print "Case #%d: NO"%(i+1)
            continue

        total = [k for k in range(n)]
        all_available_groups = []
        for j in range(1,n/2+1):
            sets = list(combine_set(total,j))
            for group in sets:
                other_group = []
                for item in total:
                    if item not in group:
                        other_group.append(item)
                if int(adder(get_items(group,bin_cs)),2) == int(adder(get_items(other_group,bin_cs)),2):
                    all_available_groups.append(group)
                    all_available_groups.append(other_group)
        
        max_val = 0
        for group in all_available_groups:
            tmp_val = 0;
            items = get_items(group,candies)
            for item in items:
                tmp_val = tmp_val + int(item)
            if tmp_val > max_val:
                max_val = tmp_val
        if len(all_available_groups) == 0:
            print "Case #%d: NO"%(i+1)
        else:
            print "Case #%d: %d"%(i+1,max_val)

