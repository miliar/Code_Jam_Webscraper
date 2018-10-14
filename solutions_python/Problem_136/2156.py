with open("B-large.in", "rt") as input:
    size = int(input.readline());
    text = input.read().split("\n");
output = open("B-large-out.out", "wt");
    
for test in range(0,size):
    line = text[test].split();
    c = float(line[0])#cost of farm
    f = float(line[1])#farm output increase
    x = float(line[2]) #win condition

    secs = 0;
    cps = 2;
    while 0 == 0:
        interval = c/cps;
        nextwintime = interval + x/(cps + f);
        wintime = x/cps;
        if wintime < nextwintime:
            secs = secs + wintime;
            break;
        else:
            secs = secs + interval;
            cps = cps + f;
    output.write("Case #" + str(test + 1) + ": " + format(secs, '0.7f') + "\n");
output.close();
