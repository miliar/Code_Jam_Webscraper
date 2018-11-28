t = int(raw_input())
f = open("output", "w")
for j in range(t):
    n, input_x = raw_input().split(" ")
    input_x = list(input_x)
    count = int(input_x[0])
    ans = 0
    for i in range(1, int(n)+1):
        if(i > count):
            ans += (i - count)
            count += (i-count)

        count += int(input_x[i])
    f.write("Case #" + str(j+1) + ": " + str(ans) + "\n")



