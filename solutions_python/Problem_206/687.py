T = input()
response = []
for t in range(1,T+1): 
    D, N = map(int, raw_input().split())
    max_arrival_time = 0
    for i in range(N):
        x, v = map(int, raw_input().split())
        arrival_time = (D - x)/float(v)
        if arrival_time > max_arrival_time:
            max_arrival_time = arrival_time
    response.append("Case #" + str(t) + ": " + str(D/max_arrival_time))
print "\n".join(response)

