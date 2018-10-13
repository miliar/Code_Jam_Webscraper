import sys
from math import ceil,floor

def schedule(cam,jam):
    jam_time = sum(map(lambda x: x[1]-x[0], cam))
    cam_time = sum(map(lambda x: x[1] - x[0], jam))

    #print(cam_time)
    #print(jam_time)

    act = cam+jam
    act.sort()
    #print(act)

    dist = [(act[i+1][0]-act[i][1], act[i][2], act[i+1][2]) for i in range(len(act)-1)]
    dist.append(((2*720-act[-1][1]+act[0][0]), act[0][2], act[-1][2]))
    dist.sort()
    #print(dist)

    switches = 0

    for diff,p1,p2 in dist:
        if p1 != p2:
            switches += 1
            cam_time += diff/2
            jam_time += diff/2
            if cam_time > 720:
                jam_time += 720-cam_time
                cam_time = 720
            elif jam_time > 720:
                cam_time += 720 - jam_time
                jam_time = 720
        else:
            if p1 == 'C':
                if jam_time + diff > 720:
                    cam_time += jam_time + diff - 720
                    jam_time = 720
                    switches += 2
                else:
                    jam_time += diff
            else:
                if cam_time + diff > 720:
                    jam_time += cam_time + diff - 720
                    cam_time = 720
                    switches += 2
                else:
                    cam_time += diff
    #print(switches)

    return switches


if __name__ == "__main__":
    name = "B-small-attempt0"
    f = open("{0}.in".format(name))
    output = open("{0}.out".format(name), "w")
    cases = int(f.readline())
    for i in range(cases):
        split = f.readline().split()
        AC = int(split[0])
        AJ = int(split[1])
        #print(N)
        #print(P)
        cam = []
        for _ in range(AC):
            split = f.readline().split()
            cam.append((int(split[0]), int(split[1]), 'C'))
        jam = []
        for _ in range(AJ):
            split = f.readline().split()
            jam.append((int(split[0]), int(split[1]), 'J'))
        output.write("Case #" + str(i + 1) + ": " + str(schedule(cam,jam)) + "\n")
    f.close()
    output.close()
