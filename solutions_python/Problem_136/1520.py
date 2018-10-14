import sys
sys.setrecursionlimit(100000)

# filename = "02-input-test"
filename = "02-B-small-attempt1"
fi = open(filename+'.in', 'r')
fo = open(filename+'.out', 'w')
lData = list()
debug = True
collect = ""
index = 0
strVal = 0

row1 = 0
cards1 = [] 
row2 = 0
cards2 = []
cases = []

for line in fi:
	if (index > 0):
		line_split = line.strip().split(' ')
		cases.append((float(line_split[0]), float(line_split[1]), float(line_split[2]), 0.0, [(0.0, 2.0, [])], []))

	index = index + 1

# print cases

def processCookies(case): 	
    C = case[0]
    F = case[1]
    X = case[2]
    T = case[3]
    list_to_process = case[4]
    new_list_to_process = list()
    list_completed =  case[5]
    
    for item in list_to_process:
        (time1, speed1, actions1) = item
        # 1. wait for cookies
        time1 = time1 + X/speed1
        actions1.append('Wait for all cookies')
        list_completed.append((time1, speed1, actions1))
        if (T == 0) or (T > time1):
            T = time1
    
        # 2. buy a farm
        (time2, speed2, actions2) = item
        time2 = time2 + C / speed2
        if (time2 < T):
            speed2 = speed2 + F
            actions2.append('Buy farm')
            new_list_to_process.append((time2, speed2, actions2))
            
    new_input = (C,F,X,T,new_list_to_process, list_completed)
    if len(new_list_to_process) > 0:
        return processCookies(new_input)
    else:
        return new_input

index = 1
solution = ""
for case in cases:
	print "Case", index, case
	sol_object = processCookies(case)
	# print index, ":::", sol_object
	# if index == 1:
		# print index, ":::", sol_object
	solution = solution + "Case #" + str(index) + ": " + str(sol_object[3]) + '\n'
	index = index + 1

solution = solution.strip()
print solution
fo.write(solution)