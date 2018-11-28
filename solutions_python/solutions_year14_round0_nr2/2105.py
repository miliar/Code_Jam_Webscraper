from decimal import *

def calculateTime( numFarms, lastTime, farmRate, target ):
   return target / ( 2 + (numFarms * farmRate)) + lastTime
   
def writeToFile( caseNum, answer ):
   outputStr = 'Case #' + str(caseNum) + ': ' + str(round(answer,7)) + '\n';
   f2.write(outputStr);

f1 = open('C:\Personal\QuickCommands\B-large.in');
f2 = open('C:\Personal\QuickCommands\cookie_output.txt', 'w');

linenum = 0;
numtests = 0

for line in f1:
   print(line);
   if linenum > 0:
      vals = line.split(' ')
      c = Decimal(vals[0]);
      f = Decimal(vals[1]);
      x = Decimal(vals[2]); 

      count = 0;
      found = False;
      farmTimes = [];
      while not found:          
         #figure out how long it would take to get to X with current number
         if len(farmTimes) > 0:
            currtime = calculateTime(len(farmTimes), farmTimes[len(farmTimes)-1], f, x);
         else:
            currtime = calculateTime(len(farmTimes), 0, f, x);         
         
         #amount of time to get to the next farm
         if len(farmTimes) > 0:
            newtime = c / ( 2 + f * len(farmTimes));
            newtime += farmTimes[len(farmTimes) -1];
         else:
            newtime = c / 2;
         
         #now we need to save off the amount of time it took to get the new farm
         farmTimes.append(newtime);
         newtime = calculateTime(len(farmTimes), newtime, f, x);
         
         #check if our new way was faster, if not our old way must have been right
         if currtime <= newtime:
            #print(currtime);
            writeToFile(linenum, currtime);
            found = True;         
         count += 1;
   linenum += 1;
f1.close()
f2.close();

