#!usr/bin/python

import sys

with open(sys.argv[1],"r") as inf:
    with open(sys.argv[2],"w") as outf:
        if inf and outf:
            # get num of cases
            T = int(inf.readline().strip())
            # parse inputs per case
            def getValues():
                return [float(i) for i in inf.readline().strip().split(" ")]

            for t in range(1,T+1):
                # C is cost of cookie farm
                # F is extre regen per cookie farm
                # X is goal
                C, F, X = getValues()
                
                time = 0.0
                cookies = 0.0
                gain = 2.0 # current gain per time

                while( cookies < X ):
                    # if build one more
                    timeBuild = C/gain + X/(gain+F)
                    # if don't build
                    timeStop = X/gain
                    if ( timeStop > timeBuild ): # better to build a cookie farm
                        time += C/gain
                        gain += F
                    else: # don't build it
                        time += X/gain
                        cookies = X
                #END while

                # print submission
                outf.write("Case #%d: %.7f\n" % (t, time))

            #END for T
        #END inf and outf
    #END open outf
#END open inf
