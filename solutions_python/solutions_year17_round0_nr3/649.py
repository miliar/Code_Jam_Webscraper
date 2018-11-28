# # input example
# 5
# 4 2
# 5 2
# 6 2
# 1000 1000
# 1000 1

# output example
# Case #1: 1 0
# Case #2: 1 0
# Case #3: 1 1
# Case #4: 0 0
# Case #5: 500 499

# assuming a tree like "empty stalls allocation" things goes as follows
# for questions email me at : ginadimaki135@gmail.com

def coverage_level(people_who_pee):

    i = 1
    level = 0
    people_left = people_who_pee
    while(i < people_left):
        level += 1
        people_left -= i
        i *= 2

    return  level, people_left

def find_ls_rs(N, level, people_left):
    num_of_max = 1
    current_max = N
    for i in range(0, level):
        # count how many maximums will be created
        if current_max%2 == 1:
            num_of_max = 2*num_of_max + (2**i - num_of_max) # i is actually how many levels exist already (before the one
            # I check right now). So 2^i is the number of tree "fathers"
        # if current_max%2 == 0 nothing changes =>  even numbers cause 1 maximum in the next level
        current_max //= 2

    if people_left > num_of_max:
        current_max -= 1

    max = current_max // 2
    min = current_max -1 -max
    return max, min

t = int(input())
for i in range(1, t + 1):
    n, k = [int(h) for h in input().split(" ")]  # read a list of integers, 2 in this case
    level, people_left = coverage_level(k)
    max, min = find_ls_rs(n, level, people_left)
    print("Case #{}: {} {}".format(i, max, min))