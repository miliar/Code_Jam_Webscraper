#file = 'B-sample'
#file = 'B-small-attempt0'
file = 'B-large'

infile = file + '.in'
outfile = file + '.out'

# read input
with open(infile) as f:
    data = f.readlines()

num = int(data[0])

data = data[1:]

output = []

for n, datum in enumerate(data):
    C, F, X = map(float, datum.split())
    
    rate = 2.0

    timetoend = X / rate
    timetofarm = C / rate
    
    timeiffarm = timetofarm + X / (rate + F)
    
    totaltime = 0
    
    end = False
    
    while not end:
        if timetoend <= timeiffarm:
            end = True
            totaltime += timetoend
        else:
            # this time has passed
            totaltime += timetofarm
    
            # update rate and farm number
            rate += F
        
            # update times
            timetoend = X / rate
            timetofarm = C / rate
            timeiffarm = timetofarm + X / (rate + F)
            
    
    output.append('Case #{}: {}'.format(n+1, totaltime))

with open(outfile, 'w') as f:
    f.write('\n'.join(output))
