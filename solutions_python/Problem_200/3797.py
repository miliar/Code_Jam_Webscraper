q = []
with open('B-large.in', 'rb') as f:
    count = 0
    for i in f:
        if count == 0:
            count = 1
            continue
        i = i.strip().decode("utf-8")
        q.append(i)

def act(num_str):
    if is_valid(num_str):
        return num_str
    num = [int(el) for el in list(num_str)]
    temp = 0
    for i in range(len(num) - 1):
        first = num[i]
        second = num[i+1]
        if first > second:
            num[i] = num[i] - 1
            temp = i+1
            break

    for i in range(temp, len(num)):
        num[i] = 9

    num = [str(el) for el in num]
    pot_ans = "".join(num)
    if is_valid(str(int(pot_ans))):
        return int(pot_ans)
    else:
        return act(pot_ans) 

def is_valid(num_str):
    num = [int(el) for el in list(num_str)]
    for i in range(len(num) - 1):
        first = num[i]
        second = num[i+1]
        if first > second:
            return False
    return True

with open('ans.txt', 'w') as f:
    for i, el in enumerate(q):
        f.write("Case #{}: {}\n".format(str(i+1), str(act(el))))

# def is_magic_number(no, case):
#     values_so_far = set([0,1,2,3,4,5,6,7,8,9])
#     my_set = set()
#     c = 0
#     if no == 0:
#         print("Case #{}: ".format(case) + "INSOMNIA")
#         return
#     while values_so_far != my_set:
#         c += 1
#         n = no * c
#         my_set = my_set.union(convert_to_digits(n))
#     print("Case #{}: ".format(case) + str(n))

# for a, val in enumerate(q):
#     is_magic_number(val, a+1)
