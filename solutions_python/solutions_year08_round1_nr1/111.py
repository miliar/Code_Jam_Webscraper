#!/usr/local/bin/python

# Final answer obtained by
# ./scriptname.py -q -i A-small.in
# or
# ./scriptname.py -q -i A-large.in

#Python 2.5.2 (r252:60911, May  6 2008, 16:32:45) 
#[GCC 4.1.2 20070626 (Red Hat 4.1.2-14)] on linux2

#snippets from http://docs.python.org/lib/module-optparse.html

# 6:00 pm PDT on Fri July 25

#linear algebra


import sys
from optparse import OptionParser
import string

def googledot(xin, yin):
    sum=0
    for i in range(0,len(xin)):
        sum+=xin[i]*yin[len(xin)-1-i]
    return sum


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
    if numcases<=0 or numcases>10000:
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
        
        try:
            veclen=int(string.strip(filein.readline()))
        except:
            print "Failed to read vector length"
            return -1

        if opts.verbose:
            print "Case %d len=%d"%(count,veclen)

        try:
            vec1=string.strip(filein.readline())
        except:
            print "Failed to read vector 1"
            return -1
        try:
            vec2=string.strip(filein.readline())
        except:
            print "Failed to read vector 2"
            return -1

        v1=[]
        v2=[]
        for v in string.split(vec1,' '):
            v1.append(int(v))
        for v in string.split(vec2,' '):
            v2.append(int(v))
        if opts.verbose:
            print v1
            print v2

        out1=sorted(v1,key=int)
        out2=sorted(v2,key=int)
        
        rval=googledot(out1,out2)

        print "Case #%d: %d"%(count,rval)
 





#############################################################

if __name__ == "__main__":
    # Process command line
    # Process it here so opts and args are global
    (opts,args)=process_args()    
    sys.exit(main())
