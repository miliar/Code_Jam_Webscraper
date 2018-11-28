#getting data
data = input ()
data = data.split('\n')
cases = int(data[0])
data = data [1:]
for c in range (0,cases):
    data[c] = data[c].split()
    for i in range(0,3):
        data[c][i] = float(data[c][i])

for case in range (0, cases):
    c = data[case][0]
    f = data[case][1]
    x = data[case][2]
    p = 2.0
    time = 0.0
    while x/p > (c/p + x/(p + f)):
        time = time + c/p
        p = p + f
    time = time + x/p
    print ('Case #' + str(case +1) + ": " + str(time))
