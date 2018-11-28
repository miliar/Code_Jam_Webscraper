def read_one():
    nfiles, capacity = map(int, input().split())
    files = list(map(int, input().split()))
    assert(len(files) == nfiles)
    return capacity, files

def solve(capacity, files):
    files.sort()
    loweri = 0
    upperi = len(files) - 1

    ndisks = 0
    while loweri < upperi:
        assert(files[loweri] <= capacity)
        assert(files[upperi] <= capacity)

        if files[loweri] + files[upperi] <= capacity:
            upperi -= 1
            loweri += 1
            ndisks += 1
        else:
            upperi -= 1
            ndisks += 1

    if upperi == loweri:
        ndisks += 1

    return ndisks


def main():
    ncases = int(input())
    for i in range(1, ncases + 1):
        disks = solve(*read_one())
        print('Case #{}: {}'.format(i, disks))


main()

