input = open("A-large-0.in")
output = open("A-large-0.out", 'w')

T = int(input.readline())

for i in xrange(1, T + 1):
    case = input.readline().split(" ")

    pairs = []
        
    for j in xrange(1, len(case), 2):
        pairs.append((case[j], int(case[j + 1])))
       
    o_pos = 1
    o_time = 0
    b_pos = 1
    b_time = 0
        
    time = 0;
        
    for button in pairs:
        if button[0] == 'O':
            time = max(abs(button[1] - o_pos) + o_time, time) + 1
            o_time = time
            o_pos = button[1]
        else:
            time = max(abs(button[1] - b_pos) + b_time, time) + 1
            b_time = time
            b_pos = button[1]

    output.write("Case #" + str(i) + ": " + str(time) + "\n")

input.close()
output.close()