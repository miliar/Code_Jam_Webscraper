__author__ = 'rutger'
out = open("out.txt", "w")
T = int(input())
for t in range(T):
    s = list(map(int, input().split()))
    a = []
    for i in range(s[0] + 1):
        a.insert(0, s[1] % 10)
        s[1] //= 10


    counter = 0
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        if sum < i+1:
            counter += 1
            sum += 1

    if t+1 < T:
        out.write("Case #%d: %d\n" % (t+1, counter))
    else:
        out.write("Case #%d: %d\n" % (t+1, counter))
    print("Case #%d: %d" % (t+1, counter))