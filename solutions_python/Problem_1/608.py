#!/usr/bin/python
import sys
from math import *

def findall(L, value):
    result = 0
    i=-1
    try:
        i=L.index( value, i+1 )
        yield i
    except ValueError:
        pass

def f(x):
    return cmp( x[1], x[2] )

def howmanyswitches(num_engines,num_queries,engine_list,query_list):

    num_switches = 0
    #engine list sort by the occurrence in query list
    query_list_len = len( query_list )

    while len(query_list)>0:
        #unique_query_list = [query_list[0]]
        #for i in range(0, len(query_list)):
		#          if cmp( unique_query_list[-1] , query_list[i] ) != 0:
	#		                   unique_query_list += query_list[i]
        for engine in engine_list:
		      print engine
		      print query_list.count(engine)
		      if query_list.count(engine) == 0:
			      return num_switches

        query_occurrences = []
        for one_query in set( query_list ):
		#query, frequency, the first index
        	query_occurrences += [[ one_query, query_list.count( one_query ), query_list.index( one_query ) ]]
        query_occurrences.sort( lambda x,y: cmp(x[1],y[1]) or cmp(y[2],x[2]) )

        print query_occurrences
        allenginesfound = 0
        if query_occurrences[0][1] != 0:
            num_switches += 1
            search_list = []
            for i in range(0,len(query_list)):
                if not (query_list[i] in search_list):
                    search_list += [query_list[i]]
                if len(search_list) >= len(engine_list):
                    query_list = query_list[i:]
                    break
	    #query_list = query_list[ query_occurrences[0][2]+1: ]
	    #query_list_len -= query_occurrences[0][2]+1


        print query_list
    	print num_switches
    return num_switches


def readinputfile( inputfilename, outputfilename ):
    inputread = open( inputfilename , "r" )
    output = open( outputfilename, "w" )

    fileLines = inputread.readlines()
    #print fileLines
    #strip the '\n' character.
    for i in range(0,len( fileLines )):
        fileLines[i] = fileLines[i].strip("\n")

    #print "numCasess=%s" % fileLines[0]

    num_cases = int( fileLines[0] )

    del fileLines[0]
    for i in range(0, num_cases):
        num_engines = int( fileLines[0] )
        engine_list = fileLines[1:num_engines+1]
        del fileLines[:num_engines+1]

        num_queries = int( fileLines[0] )
        query_list = fileLines[1:num_queries+1]
        del fileLines[:num_queries+1]

        print "Case #%d" % i
        print engine_list
        print query_list

        num_switches = howmanyswitches(num_engines,num_queries,engine_list,query_list)
        output.write( "Case #%d: %d\n" % (i+1,num_switches))

def main( inputfilename ):
        outputfilename = inputfilename[0:-3] + ".out"
        #print outputfilename

        readinputfile( inputfilename, outputfilename )

if __name__ == '__main__':
        if len(sys.argv) == 2:
                main( sys.argv[1] ) #input filename
