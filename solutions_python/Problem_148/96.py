def solve(N, X, files):
    files.sort()
    count, i, j = 0, 0, len(files) - 1
    while i <= j:
        if files[i] + files[j] <= X:
            i += 1
        j -= 1
        count += 1
    return count

def main():
    T = int(input())
    for i in range(1, T + 1):
        N, X = (int(s) for s in input().strip().split())
        files = list(int(s) for s in input().strip().split())
        disks = solve(N, X, files)
        print('Case #', i, ': ', disks, sep='')

if __name__ == "__main__":
    main()
