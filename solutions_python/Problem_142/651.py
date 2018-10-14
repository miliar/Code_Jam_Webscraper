
in_file = "A-small-attempt0.in"
out_file = "a.out"

out = open(out_file, 'w')

string_set = set()

def isRepeatable(string_list):
    string_set.clear()
    for i in range(len(string_list)):
        target = [string_list[i][0]]
        for n in range(1, len(string_list[i])):
            if string_list[i][n] != target[len(target) - 1]:
                target.append(string_list[i][n])
        string_set.add(''.join(target))
    if len(string_set) == 1:
        return True
    else:
        return False

def minimum_move(num_list):
    sort_list = sorted(num_list)
    minimum = sort_list[0]
    maximum = sort_list[len(sort_list)-1]
    result = 999
    for i in range(minimum, maximum + 1):
        count = 0
        for n in sort_list:
            count += abs(i - n)
        if count < result:
            result = count
    return result


def repeater(string_list):
    if not isRepeatable(string_list):
        return "Fegla Won"

    table = []
    target = string_set.pop()

    for s in string_list:
        count = 0
        pointer = 0
        count_list = []
        for c in s:
            if c == target[pointer]:
                count += 1
            else:
                count_list.append(count)
                count = 1
                pointer += 1
        count_list.append(count)        
        table.append(count_list)

    result = 0
    for i in range(len(target)):
        num_list = []
        for j in range(len(table)):
            num_list.append(table[j][i])
        result += minimum_move(num_list)

    return result 

def result_out(case, result):
    out.write("Case #" + str(case) + ": " + str(result) + '\n')


with open(in_file) as f:
    case_num = int(f.readline())
    for case in range(1, case_num + 1):
        string_list = []
        string_num = int(f.readline().strip())
        for n in range(string_num):
            string_list.append(f.readline().strip())
        result = repeater(string_list)
        result_out(case, result)



