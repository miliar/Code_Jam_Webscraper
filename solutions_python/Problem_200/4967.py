
f = open('numbers', 'r')


max_no = 0
count =0
next(f)
for line in f:
    if line.strip():
        n = int(line)
        for i in range(1, n+1):
            num = str(i)
            arr = list(num)
            if sorted(arr) == arr:
                max_no = i
            else:
                continue

        count = count + 1
        print('Case #' + str(count) + ':' + str(max_no))