def solution():
    D, N = [int(x) for x in input().split(" ")]
    horses = []
    for i in range(N):
        horses.append( [float(x) for x in input().split(" ")] )

    #
    # cycle through each horse taking lower limit
    # either when the horse reaches the end
    # or when the horse reaches the next horse
    #
    arrival_times = []
    for h in horses:
        arrival_times.append( float(D - h[0]) / float(h[1]) )

    value = float(D) / float(max(arrival_times))
    return value

testcases = int(input())
for i in range(testcases):
    print("Case #" + str(i+1) + ": " + str(solution()))
