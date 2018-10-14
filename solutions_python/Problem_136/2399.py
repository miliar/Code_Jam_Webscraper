# f = open('B-small-attempt1.in')
f = open('B-large.in')
count = int(f.readline())
output = ''
for x in range(1,count + 1):
    arr = f.readline().split()
    cost = float(arr[0])
    production = float(arr[1])
    goal = float(arr[2])

    # max = int(goal/cost)
    # min = 0
    # mid = max/2
    time = 0.0
    fcount = 0
    if production * goal / cost - 2 <= 0:
        time = goal/2
    else:
        fcount = int((production * goal / cost - 2)/production)

        for y in range(0,fcount+1):
            if y == fcount:
                time += goal / (fcount * production + 2)
            else:
                time += cost/(2+y*production)


    output += 'Case #' + str(x) + ': '+str(time)+'\n'


print(output)
newf = open('output.txt','w')
newf.write(output)
