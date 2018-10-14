# Return the largest tidy number M ≤ N.
def largest_tidy(n):
    digits = str(n)[::-1]
    length = len(digits)
    i = 0
    while i < length:
        if i < length-1 and digits[i] < digits[i+1]:
            digits = (str(int(digits[i+1:][::-1])*10**(i+1) - 1))[::-1]
            length = len(digits)
        i += 1
    return int(digits[::-1])

# Process input
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        solution = largest_tidy(int(input()))
        print("Case #{}: {}".format(i+1, solution))
