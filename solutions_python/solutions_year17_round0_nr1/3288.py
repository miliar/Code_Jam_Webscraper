# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def flip(arr):
    for i,_ in enumerate(arr):
        if(arr[i] == '+'):
            arr[i] = '-'
        else:
            arr[i] = '+'
    # print(arr)
    return arr

t = int(input())  # read a line with a single integer
# print(t)
for i in range(1, t + 1):
    # print(input().split(" "))
    S, k = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    S = list(S)
    k = int(k)
    flips = 0
    if '-' in S:
        for j in range(len(S)-k+1):
            if(S[j]=='-'):
                S[j:j+k] = flip(S[j:j+k])
                # print(S)
                flips += 1
        if '-' in S:
            ans = "IMPOSSIBLE"
        else:
            ans = flips
    else:
        ans = 0
    print("Case #{}: {}".format(i, ans))
    # # check out .format's specification for more formatting options
