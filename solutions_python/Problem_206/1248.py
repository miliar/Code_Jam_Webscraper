def read_input():
    line = input().split()
    dest = int(line[0])
    num_horses = int(line[1])
    max_time = float("-inf")
    for i in range(num_horses):
    	line = input().split()
    	start = int(line[0])
    	speed = int(line[1])
    	time = (dest - start) / speed
    	if time > max_time:
    		max_time = time
    return '{0:.6f}'.format(float(dest / max_time))
    

numCases = int(input())
# print(numCases)
for i in range(1, numCases + 1):
    output = read_input()
    print("Case #%d:" % i, output)