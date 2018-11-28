def solve(lines):
    l = [float(x) for x in lines[0].split(" ")]
    C = l[0]
    F = l[1]
    X = l[2]

    time=0.0
    speed=2.0
    ratio=C/F
    while(True):
        left=X/speed
        buildtime=C/speed
        build = left > (buildtime + (X/(speed+F)))
        if build:
            time+=buildtime
            speed+=F
        else:
            time+=left
            break

    return time

input_text = [line.strip() for line in open('q2l.txt')]
CASE_COUNT = int(input_text[0])
NUM_EACH_CASE = 1
for CASE_NUM in range(1,CASE_COUNT+1):
    start = (CASE_NUM-1)*NUM_EACH_CASE+1
    end = start + NUM_EACH_CASE
    arr = [x for x in input_text[start:end]]
    print "Case #%d: %0.7f" % (CASE_NUM,solve(arr))
