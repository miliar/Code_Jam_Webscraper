#! usr/bin/python
#Problem A
#Bot Trust

#Create the output list
out = list()

def run(a, read):
    opposedPs = list()
    combinePs = list()
    x = int(read[0])
    if x != 0:
        for i in read[1:x+1]:
            combinePs.append(i[:2])
            combinePs.append(i[-1])
            read.remove(i)
    read.remove(str(x))

    y = int(read[0])
    #print y
    if y != 0:
        for i in read[1:y+1]:
            opposedPs.append(i)
            read.remove(i)
    read.remove(str(y))
    #print opposedPs
    z = int(read[0])
    eToI = str(read[1])
    eI = []
    #get first element
    eI.append(eToI[0])
    eToI = eToI[1:]
    if z != 1:
        for i in eToI:
            #print i
            eI.append(i)
            eToI = eToI[1:]

            #Check to combine with last added item
            try:
                last = eI[-2] #we've already added one item
            except:
                last = None
            print 'L', last
            if last != None:
                l = -1
                t = i+last
                print "Trev:", t
                try:
                    #print "Trying"
                    l = combinePs.index(t)
                    print "go"
                    eI = eI[:-2]
                    eI.append(str(combinePs[l+1]))
                    print "G:", combinePs[l+1], eI
                except:
                    l = -1
                if l == -1:
                    t = last+i
                    print "T:", t
                    try:
                        l = combinePs.index(t)
                        eI = eI[:-2]
                        eI.append(str(combinePs[l+1]))
                        print "G:", combinePs[l+1], eI
                    except:
                        l = -1
                if l == -1:
                    for j in opposedPs:
                        print j, j[0], j[1], "J"
                        if j[0] == i:
                            try:
                                m = eI.index(str(j[1]))
                                print "FOUND... WIPING"
                                eI = []
                                print eI
                            except:
                                print "nothing happens"
                        elif j[1] == i:
                            try:
                                m = eI.index(str(j[0]))
                                print "FOUND... WIPING"
                                eI = []
                                print eI
                            except:
                                print "nothing happens"
    elements = "["
    for f in eI:
        elements += f+", "
    elements = elements[:-2]
    elements += "]"
    if elements == "]":
        elements = "[]"
    
    out = "Case #"+ str(a)+ ": "+ elements
    print out
    return out

def main():
    #Open input
    try:
        f = open('B-large.in', 'r')
    except:
        f = open('B-small-attempt0.in', 'r')
    #Get number of test cases
    n = int(f.readline())

    #For each test case get the words and runs the algorithm on it
    a = 1
    while a <= n:
        #in_line = in_line[:-1]
        #if not in_line:
        #    print "ERROR!"

        #Get all the variables from the input, in this case button presses needed
        read = f.readline()
        read = read[:-1]
        read = read.split(' ')

        #Add the output of the algorithm to the final output
        out.append(run(a, read))
        a += 1
    #print out
    f.close()

    #Write the output
    f = open('B.out', 'w')
    for x in out:
        x = str(x) + '\n'
        f.write(x)
    #f.writelines(out)
    f.close()

import psyco
psyco.full()
#import array
main()
