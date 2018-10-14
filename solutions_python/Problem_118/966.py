from math import sqrt, floor, ceil

def is_square(num):
    root = sqrt(num)
    return root == int(root)

def is_palindrome(num):
    return num == int((str(num))[::-1])


num_cases = int(raw_input())

for case in range(1, num_cases+1):
    count = 0

    limits = (raw_input()).split(" ")
    A = int(limits[0])
    B = int(limits[1])

    reduced_A = int(ceil(sqrt(A)))
    reduced_B = int(floor(sqrt(B)))

    for num in range(reduced_A, reduced_B + 1):
        if(is_palindrome(num)):
            if(is_palindrome(num*num)):
                count = count + 1

    print("Case #"+str(case)+": "+str(count))