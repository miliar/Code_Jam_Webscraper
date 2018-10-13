#Google Code Jam Submission
#Liam O'Connor-Davis
#Problem A


def main():
   file = open("test.dat","r")
   if file:
      num_cases = int(file.readline())
      i = 0
      while i < num_cases:
         print "Case #"+str(i+1)+": " + str(processCase(file))
         i = i + 1
      print ""
   return 0


def readEngines(file):
   if file:
      num_engines = int(file.readline())      
   engines = {}
   i = 0   
   while file and (i < num_engines):
      engines[file.readline()] = -1
      i = i + 1
   return engines

def readQueries(file):
   if file:
      num_queries = int(file.readline())
   queries = []
   i = 0
   while file and (i < num_queries):
      queries.append(file.readline())
      i = i + 1
   return queries


def processCase(file):
   """read and process a single case data from a file"""

   engines = readEngines(file)
   queries = readQueries(file)
   
   numchanges = -1
   startpoint = 0
   while startpoint < len(queries):   
      numchanges = numchanges + 1
      startpoint = findBest(queries,engines.copy(),startpoint)
   if (numchanges == -1):
      numchanges = 0
   return numchanges   

   
   
def findBest(queries, engines, startpoint):
   i = startpoint
   for query in queries[startpoint:]:
      if query in engines and engines[query] == -1:
         engines[query] = i        
  #       print query.strip() + " knocked out."
         if not -1 in engines.values():
   #         print "all knocked out"
            return findMaximum(engines)
      i = i + 1      
   return len(queries)
 
def findMaximum(engines):
   highest = -1
   for engine in engines.keys():
      if engines[engine] > highest:
         highest = engines[engine]
        
   return highest      


main()

