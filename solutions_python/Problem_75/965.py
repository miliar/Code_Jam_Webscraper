def main():
    test_num = int(raw_input())
    for i in range(test_num):
        string = raw_input()
        input_list = string.split()
        print "Case #"+str(i+1)+": "+solve(input_list)

def solve(input_list):
    combination = {}
    opposed = []
    combine = int(input_list.pop(0))
    for i in range(combine):
        string = input_list.pop(0)
        combination[(string[0],string[1])]=string[2]
    oppose = int(input_list.pop(0))
    for i in range(oppose):
        string = input_list.pop(0)
        opposed.append((string[0], string[1]))
    length = int(input_list.pop(0))
    string = input_list.pop(0)

    result = []

    for i in range(length):
        cur = string[i]
        last_idx = len(result)-1
        last = ''
        used = False
        if last_idx>=0:
            last = result[last_idx]
            if (last, cur) in combination:
                result.pop()
                result.append(combination[(last, cur)])
                used = True
                cur = combination[(last, cur)]
            elif (cur, last) in combination:
                result.pop()
                result.append(combination[(cur, last)])
                used = True
                cur = combination[(cur, last)]
            for x in opposed:
                find = ''
                if cur in x:
                    if cur == x[0]:
                        find = x[1]
                    if cur == x[1]:
                        find = x[0]
                if find != '':
                    if find in result:
                        result = []
                        used = True
                        break
        if not used:
            result.append(cur)

    #change list to string
    result_string = "["
    for i in range(len(result)-1):
        result_string+=result[i]
        result_string+=", "
    if len(result)!=0:
        result_string+=result.pop()
    result_string+="]"

    return result_string


if __name__=="__main__":main()
