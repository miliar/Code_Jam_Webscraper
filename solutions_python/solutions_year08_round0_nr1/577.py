# Saving the Universe
# Google Code Jam 2008
# By Robert Burns, July 17 2008

INPUTFILE = "A-large.in"
OUTFILE = "output-large.out"

infile = open(INPUTFILE)
outfile = open(OUTFILE, "w")

numCases = int(infile.readline().strip())


for casen in range(numCases):
    numEngines = int(infile.readline().strip())

    engines = []
    for engn in range(numEngines):
        engines.append(infile.readline().strip())

    numSearches = int(infile.readline().strip())

    searches = []
    required = 0
    for searchn in range(numSearches):
        search = infile.readline().strip()

        if((search in engines) and (not search in searches)):
            searches.append(search)

        if(len(engines) == len(searches)):
            searches = [search]
            required = required + 1

    output = "Case #" + str(casen + 1) + ": " + str(required)
    print output
    outfile.write(output + "\n")

        
infile.close()
outfile.close()
    
        
        
