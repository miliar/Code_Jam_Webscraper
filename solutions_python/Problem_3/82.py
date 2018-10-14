#!/usr/local/bin/python

# Final answer obtained by
# ./scriptname.py -q -i A-small.in
# or
# ./scriptname.py -q -i A-large.in

#Python 2.5.2 (r252:60911, May  6 2008, 16:32:45) 
#[GCC 4.1.2 20070626 (Red Hat 4.1.2-14)] on linux2

#snippets from http://docs.python.org/lib/module-optparse.html

# 6:46 pm on Wed July 16

# Swat flies



import sys
from optparse import OptionParser
import string
import math

def usage():
    print ""

def process_args():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="fname",
                  help="Input file name.", metavar="DIR", default="A-small.in")
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
    (opts, args) = parser.parse_args()
    return opts,args


def eval_integral(xin,rin):
    #integral if y=math.sqrt(r^2-x^2)
    u=math.sqrt(rin**2-xin**2)
    return 0.5*(xin*u+(rin**2)*math.asin(xin/rin))

def eval_integral2(x1,x2,rin):
    vx1=eval_integral(x1,rin)
    vx2=eval_integral(x2,rin)
    return vx2-vx1

def main():

    if opts.verbose:
        print "Input = "+opts.fname

    # Open the input file
    try:
        filein=open(opts.fname,"r")
    except:
        print "Failed to open "+fname        
    if opts.verbose:
        print opts.fname+" is open."

    # Read first line (the number of cases)
    try:
        numcases=int(string.strip(filein.readline()))
    except:
        print "Failed to read first line (number of cases)"
        return -1    
    if opts.verbose:
        print str(numcases)+" cases in file."

    # Check limit on num cases
    if numcases<=0 or numcases>100:
        print "   Too many cases in file. Exiting..."
        return -2
    
    # Loop over cases
    count=0
    while 1:
        count+=1
        #break after we have processed all cases
        if count>numcases:
            return 0
        if opts.verbose:
            print ""
            print "Case "+str(count)+"/"+str(numcases)
 
        # Read in the turn around time
        try:
            params1=string.strip(filein.readline())
	    params=params1.split(' ')
        except:
            print "Failed to read parameters"
            return -3
        if opts.verbose:
            print params

	flyr=float(params[0])
	racr=float(params[1])
	ract=float(params[2])
	wirr=float(params[3])
	wirg=float(params[4])

	fullarea=math.pi*racr**2
	safearea=0.0

	unsafer=racr-ract-flyr
	if opts.verbose:
	   print "   Unsafer="+str(unsafer)

        ny=0
	while 1:
            nx=0
	    while 1:
		#corners of the flies safe square
		x1=wirr+flyr+nx*(2*wirr+wirg)
		x2=-wirr-flyr+(nx+1)*(2*wirr+wirg)
		y1=wirr+flyr+ny*(2*wirr+wirg)
		y2=-wirr-flyr+(ny+1)*(2*wirr+wirg)
                nx+=1

                
		if x2<=x1 or y2<=y1:
                    if opts.verbose:
                        print "   No safe gap"
                        break

                #print (x1**2),(y1**2),(x1**2)+(y1**2),unsafer**2
                if (x1**2)+(y1**2)>=unsafer**2:
                    if opts.verbose:
                        print "   Done x loop"
                    break
                if (y1>racr):
                    if opts.verbose:
                        print "   Done y loop"
                    break
                
		if opts.verbose:
                    print "   xy1=(%5.1e,%5.1e)   xy2=(%5.1e,%5.1e)" % \
                          (x1,y1,x2,y2)


                    # Integrate safe area
                if (x2**2)+(y2**2)<=unsafer**2:
                    safearea+=(x2-x1)*(y2-y1)
                    if opts.verbose:
                        print "      %5.2e %5.2e"%(safearea,fullarea)
                    continue

                x3=x4=y3=y4=0.0

                if y1<unsafer:
                    x3=math.sqrt(unsafer**2-y1**2)
                if y2<unsafer:
                    x4=math.sqrt(unsafer**2-y2**2)
                if x1<unsafer:
                    y3=math.sqrt(unsafer**2-x1**2)
		if x2<unsafer:
		    y4=math.sqrt(unsafer**2-x2**2)

                if opts.verbose:
                    print "   xy3=(%5.1e,%5.1e)   xy4=(%5.1e,%5.1e)" % \
                          (x3,y3,x4,y4)
                    
		#integrate
                
		#1 circle cuts x1-axis at y3 and y1-axis at x3
                if x4<=x1<=x3<=x2 and y4<=y1<=y3<=y2:
                    safearea+=eval_integral2(x1,x3,unsafer)
		    #remove area below y1 from integral
                    safearea-=(y1-0.0)*(x3-x1)
                    if opts.verbose:
                        print "      #1 %5.2e %5.2e"%(safearea,fullarea)
                    continue
		#2 circle cuts x2-axis at y4 and y2-axis at x4
                if x1<=x4<=x2<=x3 and y1<=y4<=y2<=y3:
                    safearea+=(x4-x1)*(y2-y1)
                    safearea+=eval_integral2(x4,x2,unsafer)
		    #remove area below y1 from integral
                    safearea-=(y1-0.0)*(x2-x4)                    
                    if opts.verbose:
                        print "      #2 %5.2e %5.2e"%(safearea,fullarea)
                    continue
		#3 circle cuts y2-axis at x4 and y1-axis at x3
                if x1<=x4<=x3<=x2 and y4<=y1<=y2<=y3:
                    safearea+=(x4-x1)*(y2-y1)
                    safearea+=eval_integral2(x4,x3,unsafer)
		    #remove area below y1 from integral
                    safearea-=(y1-0.0)*(x3-x4)                    
                    if opts.verbose:
                        print "      #3 %5.2e %5.2e"%(safearea,fullarea)
                    continue
		#4 circle cuts y1-axis at x3 and y2-axis at x4
                if x4<=x1<=x2<=x3 and y1<=y4<=y3<=y2:
                    safearea+=eval_integral2(x1,x2,unsafer)
		    #remove area below y1 from integral
                    safearea-=(y1-0.0)*(x2-x1)
                    if opts.verbose:
                        print "      #4 %5.2e %5.2e"%(safearea,fullarea)
                    continue
                #4 and #5
                #if x1<x3 and 



            if y1>racr:
	       break
	    ny+=1


	# 4 fold symmetry
	safearea*=4.0
	prob=1.0-safearea/fullarea

        # Read in the number of trips
        print "Case #%d: %8.6f" % (count, prob)
                
                

if __name__ == "__main__":
    # Process command line
    # Process it here so opts and args are global
    (opts,args)=process_args()    
    sys.exit(main())
