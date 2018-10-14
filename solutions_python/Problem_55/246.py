import sys

def readListOfInts( inputFile ):
	return map( int, inputFile.readline().strip().split(" ") )

def LoadGroups( Groups, Capacity ):
	Onboard = Groups[:1]
	Groups = Groups[1:]
	while len(Groups) > 0 and sum(Onboard) + Groups[0] <= Capacity:
		Onboard += Groups[:1]
		Groups = Groups[1:]
	Groups = Groups + Onboard
	return (Groups, sum(Onboard))

if( len(sys.argv) > 1 ):
	input = file( sys.argv[1] )
else:
	input = file("C-tiny.in")

T = int(input.readline())

for case in range(T):
	
	(TotalRuns, Capacity, NumGroups) = readListOfInts( input )
	Groups = readListOfInts( input ) + [0]
	
	Euros = 0
	
	Runs = 1
	(Groups, Income) = LoadGroups( Groups, Capacity )
	Euros += Income
	while Runs < TotalRuns:
		Runs += 1
		(Groups, Income)= LoadGroups( Groups, Capacity )
		Euros += Income
	
	output = "Case #%d: %s" % ( case+1, Euros )
	print output