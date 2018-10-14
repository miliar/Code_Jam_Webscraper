# # input example
# 4
# 132
# 1000
# 7
# 111111111111111110

# output example
# Case #1: 129
# Case #2: 999
# Case #3: 7
# Case #4: 99999999999999999

def find_messy(num_array):

    index_twin = None

    for i in range(0, len(num_array)-1):
        if num_array[i] > num_array[i+1]:
            if index_twin:
                return index_twin+1
            return i+1
        elif num_array[i] == num_array[i+1]:
            if not index_twin:
                index_twin = i
        else:
            index_twin = None

    return "TIDY"

def tidy_up(index, num_array):
    fixed_part = ''
    for i in range(index, len(num_array)):
        fixed_part += "9"
    return fixed_part

def make_num(num_array):
    num = ""
    for n in num_array:
        num += n
    return int(num)

def find_tidy(n):
    num_array = [num for num in n]
    index = find_messy(num_array)
    if index == "TIDY":
        return n
    return find_tidy(str(make_num(num_array[:index])-1))+tidy_up(index, num_array)

t = int(input())
for i in range(1, t + 1):
    n = input()
    print("Case #{}: {}".format(i, int(find_tidy(n))))