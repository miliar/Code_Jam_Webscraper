
def main():
    t = int(input())
    for ti in range(1, t + 1):
        line = input().split()
        s_max = int(line[0])
        data = list(map(int, list(line[1])))
        print("Case #{}: {}".format(ti, solve(s_max, data)))

def solve(s_max: int, data: [int]):
    total_invites = 0
    total_standing = 0
    for shyness, count in enumerate(data):
        if count:
            invite = max(shyness - total_standing, 0)
            total_standing += invite + count 
            total_invites += invite
    assert total_standing == sum(data) + total_invites
    return total_invites

if __name__ == '__main__':
    main()
