# Hey there. -- Joshua Allum --
# Prints the largest tidy number less than N
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N = int(input())
    last_tidy = N
    digits = []
    while N != 0:
        digits.append(N % 10)
        N //= 10
    index = len(digits) - 1
    critical_index = index
    diff = True # true if the current and next indexes are different
    untidy = False
    while index > 0:
        # Find critical index
        if digits[index] > digits[index - 1]:
            untidy = True
            if diff:
                critical_index = index
            break
        elif digits[index] == digits[index - 1]:
            # critical index only changes if the two subsequent
            # numbers being compared are different
            if diff:
                critical_index = index
                diff = False
        else:
            diff = True
        index -= 1
    if untidy:
        digits[critical_index] -= 1
        last_tidy = 0
        index = len(digits) - 1
        while index >= 0:
            # Reconstructs the number
            if index >= critical_index:
                last_tidy += digits[index] * 10 ** index
            else:
                last_tidy += 9 * 10 ** index
            index -= 1
    print("Case #{}: {}".format(i, last_tidy))
        
    
