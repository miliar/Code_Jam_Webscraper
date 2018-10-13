

def solve_case(case_number):
    shy_counts = map(int, raw_input().split()[1])
    standing = 0
    friends = 0
    for i in range(len(shy_counts)):
        if standing < i:
            friends += i - standing
            standing = i + shy_counts[i]
        else:
            standing += shy_counts[i]
    print "Case #" + str(case_number) + ": " + str(friends)


def main():
    T = int(raw_input())
    for i in range(1, T + 1):
        solve_case(i)

main()
