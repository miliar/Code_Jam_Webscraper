#!/usr/bin/python
from sys import argv


def calculate_time(dist, walk_speed, run_speed, run_time, walkways):
    time=0
    walkways_distance=0
    for i in xrange(len(walkways)):
        walkways_distance+=walkways[i][0]
    if run_speed*run_time <= dist-walkways_distance:
        for i in xrange(len(walkways)):
            time+=float(walkways[i][0])/float(walk_speed+walkways[i][1])
        time+=run_time+float(dist - walkways_distance - run_speed*run_time)/float(walk_speed)
    else:
        if dist-walkways_distance>0:
            time += float(dist-walkways_distance)/float(run_speed)
            run_time=run_time-time
        while run_time > 0 and len(walkways) > 0:
            slower=0
            for i in xrange(len(walkways)):
                if walkways[i][1]<=walkways[slower][1]:
                    slower=i
            running_time=float(walkways[slower][0])/float(run_speed+walkways[slower][1])
            if running_time > run_time:
                time +=run_time + float(walkways[slower][0]-run_time*(walkways[slower][1]+run_speed))/float(walkways[slower][1]+walk_speed)
                run_time=0
                walkways.pop(slower)
            else:
                time+=running_time
                run_time=run_time-running_time
                walkways.pop(slower)
        if len(walkways)>0:
            for x in walkways:
                time+=float(x[0])/float(x[1]+walk_speed)
    return time



def walkways(input_file, output_file):
    f=open(input_file, 'r')
    N=int(f.readline())
    g=open(output_file, 'w')
    for i in xrange(N):
        line=f.readline()
        x=line.split(' ')
        ways=[]
        for j in xrange(int(x[4])):
            line=f.readline()
            xx=line.split(' ')
            ways.append([int(xx[1]) - int(xx[0]), int(xx[2])])      
        stat=calculate_time(int(x[0]), int(x[1]), int(x[2]), int(x[3]), ways)
        g.write('Case #'+str(i+1)+': ')
        g.write(str(stat)+'\n')
    f.close()
    g.close()


#run: python walkways.py input output
if __name__=='__main__':
    if argv[0].find('walkways.py')!=-1:
        if len(argv)>=3:
            walkways(argv[1], argv[2])
