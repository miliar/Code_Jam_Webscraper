import sys
sys.stdin = open("C:/Users/tobia/Desktop/Programming Contests/Code Jam 2017/B-large.in")
sys.stdout = open("B-large.out", "w")

t = int(input())
for case in range(1, t+1):
    n = input()
    arr = [0] + [int(x) for x in n]
    s = len(arr)
    doubles = 0
    ans = ""
    for i in range(1, s-1):
        if arr[i] == arr[i-1]:
            doubles += 1
        else:
            doubles = 0
        if arr[i+1] < arr[i]:
            arr[i-doubles] -= 1
            for j in range(i-doubles+1, s):
                arr[j] = 9
            ans = "".join(str(x) for x in arr[1:])
            break
    else:
        ans = n
    print("Case #{}: {}".format(case, int(ans)))

sys.stdout.close()
