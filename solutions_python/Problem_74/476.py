from sys import argv, exit

if len(argv) < 3:
    exit("Not enough arguments")

input_file = argv[1]
output_file = argv[2]



with open(output_file, 'w') as out_desc:
    in_desc = open(input_file)
    num_cases = int(in_desc.readline().strip())
    for t in xrange(num_cases):
        parts = in_desc.readline().split()

        status = {'O': (1,0), 'B': (1,0)}

        count = 0

        N = int(parts[0])
        i = 1
        for _ in xrange(N):
            color = parts[i]
            button = int(parts[i+1])
            i += 2

            distance = abs(button-status[color][0])
            time = count-status[color][1]

            count += max(0, distance-time) + 1
            status[color] = (button,count)





        print >> out_desc, "Case #%d: %s" % (t+1,count)