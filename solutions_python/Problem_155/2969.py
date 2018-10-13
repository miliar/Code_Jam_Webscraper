
input_file = open("input")
output_file = open("output", mode='w')

T = int(input_file.readline())

for t in range(T):
    row = input_file.readline().rstrip('\n')
    s_max, string = row.split(" ")
    s_max = int(s_max)

    count = 0
    friends = 0
    for s, c in enumerate(string):
        c = int(c)
        if s > count:
            friends += s-count
            count += c+(s-count)
        else:
            count += c
    output_file.write("Case #%s: %s\n" % (t+1, friends))
output_file.close()
input_file.close()
