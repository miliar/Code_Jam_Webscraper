#!/usr/bin/env python
import pprint

inputfilename = "A-small-attempt0.in"
outputfilename = "A-small-attempt0.out"

def q1(cases):
    output = ""
    casenumber = 0
    for case in cases:
        casenumber = casenumber + 1
        n = int(case.strip().split(" ")[0])
        k = int(case.strip().split(" ")[1])
        snapperlist = build_snappers(n)
        for i in range(k):
            snip(snapperlist)
        lamp = "OFF"
        if snapperlist[-1]['power'] and snapperlist[-1]['state']:
            lamp = "ON"
        output = output + "Case #%s: %s\n" % (casenumber, lamp)
    return output

def build_snappers(n):
    snapperlist = []
    for i in range(n):
        snapperlist.append({'id': i, 'state':False, 'power':False})
    snapperlist[0]['power'] = True
    return snapperlist
    
def snip(snapperlist):
    for x in range(len(snapperlist)):
        if snapperlist[x]['power'] == True:
            snapperlist[x]['state'] = not snapperlist[x]['state']
        else:
            break
            
    for x in range(len(snapperlist)):
        if x+1 < len(snapperlist):
            if snapperlist[x]['power'] == True and snapperlist[x]['state'] == True:
                snapperlist[x+1]['power'] = True
            else:
                snapperlist[x+1]['power'] = False

def main():
    inputfile = open(inputfilename, 'r')
    num_of_cases = int(inputfile.readline())
    cases = inputfile.readlines()
    inputfile.close()
    
    output = q1(cases)
    
    outputfile = open(outputfilename,'w')
    outputfile.write(output)
    outputfile.close()
    return 0


if __name__ == '__main__': main()
