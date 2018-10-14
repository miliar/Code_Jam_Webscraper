def main():
    for testcase in range(1, int(input()) + 1):
        print(f"Case #{testcase}: {solve()}")

def first_non_decreasing_index(number):
    for i in range(1, len(number)):
        if number[i-1] > number[i]:
            return i
    return None

def one_iteration(number):
    i = first_non_decreasing_index(number)
    if not i:
        return number
    assert i in range(len(number))
    left = number[:i-1]
    mid = str(int(number[i-1]) - 1)
    right = '9' * (len(number) - (i-1) - 1)
    #print(left, mid, right)
    number = left + mid + right
    number = str(int(number))  # Get rid of trailing zeroes
    return number


def solve():
    number = input().strip()
    for _ in range(21):
        number = one_iteration(number)
    return number

main()
