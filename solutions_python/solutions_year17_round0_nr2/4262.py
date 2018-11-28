import copy

def process_file(source_file, output_file):
    with open(source_file) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    if len(content) < 2:
        return
    content.pop(0)
    target = open(output_file, 'w')
    ind = 1
    for num in content:
        num_list = [int(x) for x in list(num)]
        if len(num_list) > 1 and sorted(num_list) != num_list:
            lst = [0]*len(num_list);
            for idx in xrange(0, len(num_list)-1):
                if num_list[idx] > num_list[idx+1]:
                    lst[idx] = num_list[idx] - 1
                    if lst[idx] < lst[idx-1]:
                        for i in xrange(idx, -1, -1):
                            if lst[i - 1] < lst[i]:
                                lst[i] -= 1
                                idx = i
                                break
                    for i in xrange(idx+1, len(num_list)):
                        lst[i] = 9
                    break
                else:
                    lst[idx] = num_list[idx]
            if lst[0] == 0:
                lst.pop(0)
            num_list = lst
        target.write("Case #{ind}: {num}\n".format(ind=ind, num=''.join(str(e) for e in num_list)))
        ind += 1


#process_file('B-small-attempt5.in', 'B-small-attempt5.out')
process_file('B-large.in', 'B-large.out')
#process_file('problem2-test', 'problem2-test-output')