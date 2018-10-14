def solve(line):
    arr = line.split()
    k = int(arr[1])
    arr = list(arr[0])
    rlt = 0
    for i in range(len(arr) - k + 1):
        if arr[i] == '-':
            for j in range(k - 1):
                arr[i + 1 + j] = '+' if arr[i + 1 + j] == '-' else '-'
            rlt += 1
    for i in range(len(arr) - k + 1, len(arr)):
        if arr[i] == '-':
            return 'IMPOSSIBLE'
    return rlt