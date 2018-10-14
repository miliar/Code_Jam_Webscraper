def trains(turn_around, depart, arrive):
    A = [[a,-1] for a in depart] + [[b+turn_around,1] for b in arrive]
    A.sort(lambda x,y:cmp(x[0],y[0]))
    avaliable_trains = 0
    beginning_trains = 0
    prev = -1
    B = []
    for a in A:
        if a[0] != prev:
            B.append(a)
        else:
            B[-1][1] += a[1]
        prev = a[0]
        
    for b in B:
        avaliable_trains = avaliable_trains + b[1]
        if avaliable_trains < 0:
            beginning_trains = beginning_trains - avaliable_trains
            avaliable_trains = 0
    return beginning_trains

try: 
    import sys
    filename = sys.argv[1] 
except: 
    filename = 'B-large.in'
inputfile = open(filename)
outputfile = open('output.txt','w') 

number_of_input_sets = int(inputfile.readline()) #N
for input_set in range(number_of_input_sets):
    turn_around = int(inputfile.readline())
    [NA, NB] = [int(i) for i in inputfile.readline().rstrip().split(' ')]
    Abegin = []
    Aend = []
    for a in range(NA):
        time = inputfile.readline().rstrip().split(' ')
        times = time[0].split(':')
        Abegin.append(int(times[0])*60 + int(times[1]))
        times = time[1].split(':')
        Aend.append(int(times[0])*60 + int(times[1]))
    Bbegin = []
    Bend = []
    for b in range(NB):
        time = inputfile.readline().rstrip().split(' ')
        times = time[0].split(':')
        Bbegin.append(int(times[0])*60 + int(times[1]))
        times = time[1].split(':')
        Bend.append(int(times[0])*60 + int(times[1]) )
    outputA, outputB = trains(turn_around,Abegin,Bend), trains(turn_around,Bbegin,Aend)
    outputfile.write('Case #' + str(input_set+1) + ': ' + str(outputA) + ' ' + str(outputB) + '\n')