"""

idea:
walk left-to-right over numbers
if a pair (a,b) is not sorted, replace it with (a-1,9)
loop until done

if there are zeroes, we subtract until they're gone

"""


# possible edge case: negative number in the list


def sort(n):
    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]:
            swapped = n[:i] + [n[i] - 1] + ([9] * (len(n) - i - 1))
            return sort(swapped)
    return n


def main():
    t = int(input())

    for tc in range(t):
        n = [int(x) for x in input()]
        res = sort(n)
        res = [x for x in res if x > 0]
        res = int("".join(map(str, res)))
        print("Case #{}: {}".format(tc + 1, res))


def test():
    print("t1", sort([int(x) for x in "132"]), "want", 129)
    print("t2", sort([int(x) for x in "1000"]), "want", 999)
    print("t3", sort([int(x) for x in "7"]), "want", 7)
    print("t4", sort([int(x) for x in "111111111111111110"]), "want", 99999999999999999)
    print("t10", sort([int(x) for x in "56879"]), "want", 56799)
    print("t11", sort([int(x) for x in "110"]), "want", 99)
    print("t12", sort([int(x) for x in "0100"]), "want", 99)


# test()
main()
