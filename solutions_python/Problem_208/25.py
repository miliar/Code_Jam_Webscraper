from Queue import *

level = __file__.split("\\")[-1][0]
file_is_small = 0
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

def test_case():
    [N,Q] = [int(x) for x in input_file.readline().split()]
    horses = []
    for i in xrange(N):
        horses.append([int(x) for x in input_file.readline().split()])
    maximum_time = sum([float(x[0])/float(x[1]) for x in horses])
    distances = []
    times = [[maximum_time for i in xrange(N)] for j in xrange(N)]
    for i in xrange(N):
        distances.append([int(x) for x in input_file.readline().split()])
        times[i][i] = 0.0

    for city in xrange(N): #calculate time from city to others on horse from #city
        [dist,speed] = horses[city]
        speed = float(speed)
        q = Queue()
        q.put([city,dist])
        while(not q.empty()):
            [c,d] = q.get()
            for neighbor in xrange(N):
                to = distances[c][neighbor]
                if(to != -1 and to <= d):
                    time = float(dist-d+to)/speed 
                    if(time < times[city][neighbor]):
                        times[city][neighbor] = time
                        q.put([neighbor,d-to])

    answers = []
    for query in xrange(Q):
        [source,dest] = [int(x)-1 for x in input_file.readline().split()]
        time_to = [maximum_time] * N
        time_to[source] = 0.0
        q = Queue()
        q.put([source,0.0])
        while(not q.empty()):
            [c,t] = q.get()
            for neighbor in xrange(N):
                if(c == neighbor):
                    continue
                time = time_to[c] + times[c][neighbor]
                if(time < time_to[neighbor]):
                    time_to[neighbor] = time
                    q.put([neighbor+0,time+0])
        
        answers.append(str(time_to[dest]))
    
    return " ".join(answers) 
    
T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    print out
    output_file.write(out + "\n")
    
input_file.close()
output_file.close()
