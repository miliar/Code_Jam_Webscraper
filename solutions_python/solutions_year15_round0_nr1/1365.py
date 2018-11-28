num_cases = input()
cases = []

for x in range(num_cases):
    line = raw_input().split()
    s_max = int(line[0])
    s_string = line[1]
    cases.append((s_max, s_string))

counter = 0

for case in cases:
    
    counter += 1
    total = 0
    needed = 0
    s_max = case[0]
    s_string = case[1]
    
    for char_x in range(len(s_string)):
        if char_x > total:
            needed += 1
            total += 1
        total += int(s_string[char_x])

    print "Case #" + str(counter) + ":", needed
