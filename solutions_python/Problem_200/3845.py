def tidy_checker(arg):
    if 0 < arg < 10:
        return arg
    elif arg <= 0:
        return "Number should not be less than 1"
    else:
        lst = [int(i) for i in str(arg)]
        if sorted(lst) == lst:
            return arg
        else:
            for length in range(len(lst)-1):
                if lst[length] > lst[length+1]:
                    lst[length] = lst[length]-1
                    for index in range(length+1, len(lst)):
                        lst[index] = 9
            return tidy_checker(int(''.join(map(str, lst))))


t = int(input())  # read a line with a single integer
if 0 < t < 10001:
    for x in range(1, t + 1):
        try:
            y = int(input())
            print("Case #{}: {}".format(x, tidy_checker(y)))
        except ValueError:
            print("Number must be an positive integer")
else:
    print("max number of test case must be between 1 to 100")
