def answer(case, ans):
    print("Case #{0}: {1}".format(case, ans))


def main():
    case = 1
    num_cases = int(input())
    while case <= num_cases:
        data = input().split()
        shy_distribution = [int(x) for x in data[1]]
        total_people = sum(shy_distribution)
        standing = shy_distribution[0]
        ans = 0
        if len(shy_distribution) > 1:
            for i, j in enumerate(shy_distribution[1:]):
                shyness = i + 1
                if standing < shyness:
                    diff = shyness - standing
                    ans += diff
                    standing += diff
                standing += j
        answer(case, ans)
        case += 1

if __name__ == '__main__':
    main()
