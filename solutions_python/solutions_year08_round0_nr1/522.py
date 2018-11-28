#!/usr/bin/env python

#Author : Cherif YAYA
#email : <chef.ya@gmail.com>

#Algorithm:
#I'm using a greedy algorithm. I have table of search engines.
#Queries are in a queue. For each query, I cross out the corresponding search
#engine name in the table. Queries are removed as soon as there have been
#processed.
#When every search engines of the table are crossed out, a switch need to take
#place.
#then, the table is reinitialized and we start consuming queries all over again
#until there are no more to be consumed

#dictionary containing search engines
engines = {}
#number of search engines not available for crossing
engines["CherifYAYA"] = 0

#list containing queries (used as a queue)
queries = []


def clear():
    global queries
    global engines
    queries = []
    engines = {}
    #number of search engines not available for crossing
    engines["CherifYAYA"] = 0
    

def resetEngines():
    for e in engines.keys():
        engines[e] = False
    engines["CherifYAYA"] = len(engines)-1


def crossEngine(engine):
    if engine in engines:
        if not engines[engine]:
            engines[engine] = True
            #number number of engines available for crossing
            if(engines["CherifYAYA"] >0):
                engines["CherifYAYA"] = engines["CherifYAYA"] - 1


def addEngine(engine):
    if not (engine in engines):
        engines[engine] = False
        engines["CherifYAYA"] = engines["CherifYAYA"] + 1

def consumateQueries():
    global engines
    global queries
    resetEngines()
    tmp = ""
    while(engines["CherifYAYA"] != 0 and len(queries) != 0):
        crossEngine(queries[0])
        tmp = queries[0]
        queries = queries[1:]
    #put back last query
    if(engines["CherifYAYA"] == 0):
        queries.insert(0,tmp)


def readInput(filename):
    global engines
    global queries
    f = file(filename,"r")
    out = file(filename+".out","w")
    line = f.readline()
    N = eval(line)
    i = 0
    while i < N:
        #reset fields
        clear()
        #start reading case
        S = eval(f.readline())
        j = 0
        while j<S:
            j = j+1
            addEngine(f.readline().strip())
        Q = eval(f.readline())
        j = 0
        while j < Q:
            j = j+1
            queries.append(f.readline().strip())
        nbSwitches = -1 #first switch doesn't count
        while len(queries) != 0:
            consumateQueries()
            nbSwitches = nbSwitches + 1
        if nbSwitches == -1:
            nbSwitches = 0
        #write result to output
        print "Case #%d: %d" % (i+1,nbSwitches)
        print >> out, "Case #%d: %d" % (i+1,nbSwitches)
        i = i+1
    f.close()
    out.close()

if __name__ == "__main__":
    readInput("A-large.in")
        
        
                
