import sys
sys.setrecursionlimit(5000)

def last_tidy(number_list, last_big):
    if (number_list == []): return []
    if number_list[0] < last_big: return -1

    # Test if first number is > then last_big, if so,
    # Try finding a tidy number whose first number is the same number,
    if number_list[0] >= last_big:
        recurse_answer = last_tidy(number_list[1:], number_list[0])

        if (recurse_answer != -1):
            constructed_number_list = [number_list[0]] + recurse_answer
            return constructed_number_list

    if (number_list[0] == last_big):
        return -1

    # else return number_list - 1, then number_list - 1
    constructed_number_list = []
    constructed_number_list.append(number_list[0] - 1)
    for i in range(1,len(number_list)): constructed_number_list.append(9)
    return constructed_number_list

cases = int(input(""))

for i in range(1, cases+1):
    number_list = [int(x) for x in list(input(""))]

    answer = last_tidy(number_list,0)
    while (len(answer) > 1 and answer[0] == 0): answer = answer[1:]
    answer = "".join([str(x) for x in answer])

    print("Case #%d: %s" % (i, answer))