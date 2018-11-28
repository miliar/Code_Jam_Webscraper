def find_idx_of_max(num_list):
    maximum = max(num_list)
    idx = num_list.index(maximum)
    return idx

def find_max_min(num):
    if num <= 1:
        return 0, 0
    elif num == 2:
        return 1, 0
    elif num % 2 == 0: #even
        value = num / 2
        return value, value - 1
    else: # odd
        value = (num - 1) / 2
        return value, value

read_file = open('C-small-1-attempt1.in', 'r')
write_file = open('result.txt.small', 'w')

count = 0

for line in read_file:
    if count == 0:
        t = int(line.strip())
    else:
        num_stall, num_people = line.strip().split(' ')
        num_list = [int(num_stall)]
        for dummy_idx in range(0, int(num_people)):
            idx_of_max = find_idx_of_max(num_list)
            maximum, minimum = find_max_min (num_list[idx_of_max])
            #print 'idx_of_max: ' + str(idx_of_max)
            begin_list = num_list[:idx_of_max] # beginning of the num_list
            end_list = num_list[idx_of_max + 1:] # ending of the num_list
            #print begin_list, end_list
            if minimum != 0:
                new_num_list = begin_list + [minimum] + [0] + [maximum] + end_list
            else:
                new_num_list = begin_list + [minimum] + [maximum] + end_list
            #print num_list, new_num_list
            num_list = new_num_list
            dummy_idx += 1
            #print ""
        if count != t:
            write_file.write("Case #" + str(count) + ': ' + str(maximum) + ' ' + str(minimum) + '\n')
        else:
            write_file.write("Case #" + str(count) + ': ' + str(maximum) + ' ' + str(minimum))
    count+=1
"""
num_list = [1,1,0,3,1,1]
idx_of_max = find_idx_of_max(num_list)
maximum, minimum = find_max_min (num_list[idx_of_max])
print 'idx_of_max: ' + str(idx_of_max)
begin_list = num_list[:idx_of_max] # beginning of the num_list
end_list = num_list[idx_of_max + 1:] # ending of the num_list
print begin_list, end_list
if minimum != 0:
    new_num_list = begin_list + [minimum] + [0] + [maximum] + end_list
else:
    new_num_list = begin_list + [minimum] + [maximum] + end_list
print num_list, new_num_list
num_list = new_num_list
"""