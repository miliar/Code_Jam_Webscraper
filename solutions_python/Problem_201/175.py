
def stall_wars(n, k):
    # range is odd -> two equal subproblems, consider ppl in batches of 2
    #  because subproblems are equivalent, left side will be filled first
    # range is even -> two subproblems size a and a+1,
    #  right side is filled first, then left
    #  result will be 1 even subproblem and 1 odd subproblem,
    #  order depends on a.

    if n % 2 == 0:
        left_space = (n // 2) - 1
        right_space = (n // 2)
        if k == 1:
            return (right_space, left_space)
        else:
            # You're going to fill the right side and then the left side
            # in an alternating fashion for the rest of the k ppl.
            # We can figure out what side it is using modulo,
            # then solve only that subproblem.
            k -= 1 # place the middle person
            if k % 2 == 0: # left side
                return stall_wars(left_space, k // 2)
            else: # right side
                return stall_wars(right_space, (k + 1) // 2)
    else:
        subproblem_size = (n - 1) // 2
        if k == 1:
            return (subproblem_size, subproblem_size)
        else:
            k -= 1 # place the middle person
            new_k = ((k - 1) // 2) + 1 # 1 and 2 same, 3 and 4 same, etc.
            return stall_wars(subproblem_size, new_k)


num_cases = int(input())

for i in range(num_cases):
    case_string = input()
    result = stall_wars(int(case_string.split(' ')[0]), int(case_string.split(' ')[1]))
    print("Case #" + str(i + 1) + ": " + str(result[0]) + " " + str(result[1]))
