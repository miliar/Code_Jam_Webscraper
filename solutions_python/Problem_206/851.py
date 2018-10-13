# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(input())  # read a line with a single integer

for i in range(1, T + 1):
    D, N = [int(s) for s in input().split(" ")]

    longest_time = -1.0

    for horse in range(1,N+1):
        k, s = [int(s) for s in input().split(" ")]

        if ( D - k ) / s >= longest_time:
            longest_time = (D-k)/s

    speed = D / longest_time


    print("Case #{}: {}".format(i, speed))
