import sys

in_file = open(sys.argv[1], "r")

out_file = open("output.out", "w")

t = int(in_file.readline())

for i in range(t):
    params = in_file.readline().split(' ')
    d = int(params[0])
    params = in_file.readline().split(' ')
    p = []
    for j in params:
        p.append(int(j))
    time_to_eat = max(p)

    for z in range(2, max(p)):
        steps_to_break = 0
        for k in p:
            steps_to_break += (k - 1) / z
        time_to_eat = min(time_to_eat, steps_to_break + z)


    out_file.write("Case #" + str(i + 1) + ": " + str(time_to_eat))

    out_file.write("\n")

in_file.close()
out_file.close()
