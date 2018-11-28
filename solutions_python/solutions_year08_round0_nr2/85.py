#!/usr/local/bin/python

# Final answer obtained by
# ./scriptname.py -q -i A-small.in
# or
# ./scriptname.py -q -i A-large.in

#Python 2.5.2 (r252:60911, May  6 2008, 16:32:45) 
#[GCC 4.1.2 20070626 (Red Hat 4.1.2-14)] on linux2

#snippets from http://docs.python.org/lib/module-optparse.html

# 5:33 pm on Wed July 16

# Saving the universe



import sys
from optparse import OptionParser
import string


def usage():
    print sys.argv[0]," --from=dir --to=dir"

def process_args():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="fname",
                  help="Input file name.", metavar="DIR", default="A-small.in")
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
    (opts, args) = parser.parse_args()
    return opts,args

def process_next_case(filein,case=0):
    # Read the next line
    try:
        nextline=string.strip(filein.readline())
    except:
        return -1  
    if len(nextline)<=0:
        return -2

    #Process the line
    if opts.verbose:
        print nextline,len(nextline)
    vars=nextline.split(' ')
    if len(vars)<>3:
        return -3

    numin=vars[0]
    lang1=vars[1]
    lang2=vars[2]
    if opts.verbose:
        print numin,lang1,lang2
    
    value="0"
#    value=langtodecimal(numin,lang1)
#    value=decimaltolang(value,lang2)


    print "Case #"+str(case)+":  "+value

    return 1



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
            turntime=int(string.strip(filein.readline()))
        except:
            print "Failed to read turn time"
            return -3
        if opts.verbose:
            print "   %d minutes to turn train." % turntime

        # Read in the number of trips
        try:
            numab=string.strip(filein.readline())
        except:
            print "Failed to read number of trips"
            return -3
            
        numtrips=numab.split(' ')
        for i in range(len(numtrips)):
            numtrips[i]=int(numtrips[i])
        
        if opts.verbose:
            print "   %d trips from A to B" % numtrips[0]
            print "   %d trips from B to A" % numtrips[1]

        triplines=[]
        tripstart=[]
        tripend=[]
        for i in range(numtrips[0]+numtrips[1]):
            ctrip1=string.strip(filein.readline())
            triplines.append(ctrip1)
            ctrip2=ctrip1.split(' ');
            hourmin1=ctrip2[0].split(':')
            hourmin2=ctrip2[1].split(':')
            tripstart.append(int(hourmin1[0])*60+int(hourmin1[1]))
            tripend.append(int(hourmin2[0])*60+int(hourmin2[1]))
        if opts.verbose:
            print triplines
            print tripstart
            print tripend
        


        # Find answer
        traintime=[]
        trainisat=[]
        trainstart=[]
        curtime=0
        while 1:
            tc=0
            dealwithtime=-1
            mintime=24*60+1
            for ctime in tripstart:
                tc+=1
                if ctime<0:
                    continue
                if ctime<mintime:
                    mintime=ctime
                    dealwithtime=tc
            if dealwithtime<0:
                break            
            cstart=tripstart[dealwithtime-1]
            cend=tripend[dealwithtime-1]+turntime
            if opts.verbose:
                print "   depart=%5.2f arrive&turn=%5.2f" % \
                      (cstart/60.0,cend/60.0)
            tripstart[dealwithtime-1]=-1
            if dealwithtime>numtrips[0]:
                cstation=2
            else:
                cstation=1
            if opts.verbose:
                print "   Dealing with departure %d @ %d %5.2f" % \
                      (dealwithtime, cstation, cstart/60)

            foundtrain=0
            for i in range(len(traintime)):
                if opts.verbose:
                    print "Train %d will be at %d at %5.2f" % \
                          (i+1,trainisat[i],float(traintime[i]/60.0))
                if traintime[i]<=cstart and trainisat[i]==cstation:
                    foundtrain=1
                    usetrain=i
                    break
            if foundtrain==0:
                if cstation==1:
                    trainisat.append(2)
                else:
                    trainisat.append(1)
                traintime.append(cend)
                trainstart.append(cstation)
                if opts.verbose:
                    print "   Using new train #%d" % len(traintime)
            else:
                if opts.verbose:
                    print "   Reusing train #%d" % (usetrain+1)
                if cstation==1:
                    trainisat[usetrain]=2
                else:
                    trainisat[usetrain]=1
                traintime[usetrain]=cend
        numa=0
        numb=0
        for ct in trainstart:
            if ct==1:
                numa+=1
            if ct==2:
                numb+=1
        print "Case #%d: %d %d" % (count,numa,numb)
                
                

if __name__ == "__main__":
    # Process command line
    # Process it here so opts and args are global
    (opts,args)=process_args()    
    sys.exit(main())
