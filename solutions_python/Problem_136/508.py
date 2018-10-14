
from datetime import datetime

if __name__ == "__main__":

    fin = "../in/large.in"
    fou = "../out/large.out"

    stt = datetime.now()

    inf = open(fin,"r")
    ouf = open(fou,"w")

    cases = int(inf.readline())
    for t in range(cases):
        farms, exits, tots  = [], [], []            # Times to get new farms, all cookies, total elapsed times
        found = False
        cfx = map(float,inf.readline().split())     # Get C, F, X from file
        cps = 2.0                                   # Cookies per second
        running_farms_times = 0.0
        idx = 0
        while not found:
            farms.append(cfx[0]/cps)                # Calculate time to next farm
            exits.append(cfx[2]/cps)                # Calculate time to exit
            if idx == 0:
                tots.append(cfx[2]/cps)             # First run through, simply add time to exit
            else:
                tots.append((cfx[2]/cps) + running_farms_times)     # Subsequent tries, add time to exit + sum of all preceding farm purchases
                if tots[idx] > tots[idx-1]:                         # If new time is longer than previous run, answer is found
                    ans = tots[idx-1]
                    found = True

            running_farms_times += farms[idx]       # Add to running farms counter
            cps += cfx[1]                           # Increment cookies per second
            idx += 1                                # Increment index counter

        ouf.write("Case #%d: %.7f\n" % ((t+1), ans))

    inf.close()
    ouf.close()

    print "Answer in: " + str(datetime.now() - stt)
