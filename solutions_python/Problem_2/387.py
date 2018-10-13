#!/usr/bin/python

import sys;
import re;

def schedule_trains(trips_A, trips_B, T):
   available_A = [];
   available_B = [];
   nA = 0;
   nB = 0;

   while( (len(trips_A)>0) or (len(trips_B)> 0) ):
      # find next trip

      # A -> B
      if((len(trips_B) == 0 ) or ((len(trips_A) >  0 ) and (trips_A[0] < trips_B[0]))):
         trip = trips_A.pop(0);
	 # print "A->B: " + str(trip[0]) + " :: " + str(trip[1]) + "::" + str(trip[1] + T);
	 # print "\tavailable trains: " + str(available_A);

	 # look at first available train
	 if((len(available_A) > 0) and (trip[0] >= available_A[0])):
	    # print "\tusing " + str(available_A[0]);
	    available_A.pop(0);

	 # if nothing is available, add a train
	 else:
	    # print "\tno trains available at " + str(trip[0]) + ", creating one";
	    nA += 1;

	 # make this train available in B  T minutes after it arrives
	 available_B.append(trip[1] + T);
	 available_B.sort();
	 # print "\ttrain placed in availableB: " + str(available_B);

      # B-> A
      else:
         trip = trips_B.pop(0);
	 # print "B->A: " + str(trip[0]) + " :: " + str(trip[1]) + "::" + str(trip[1] + T);
	 # print "\tavailable trains: " + str(available_B);

	 # look at first available train
	 if((len(available_B) > 0) and (trip[0] >= available_B[0])):
	    # print "\tusing " + str(available_B[0]);
	    available_B.pop(0);

	 # if nothing is available, add a train
	 else:
	    # print "\tno trains available at " + str(trip[0]) + ", creating one";
	    nB += 1;

	 # make this train available in A  T minutes after it arrives
	 available_A.append(trip[1] + T);
	 available_A.sort();
	 # print "\ttrain placed in availableA: " + str(available_A);

   return nA, nB;



# read in file
file = open(sys.argv[1], "r");

N = int(file.readline());

for i in range(N):
   T = int(file.readline());

   # read NA and NB
   line = file.readline();
   m = re.search(r"(?P<NA>\d+) (?P<NB>\d+)", line);
   NA = int(m.group("NA"));
   NB = int(m.group("NB"));

   trips_A = [];
   trips_B = [];

   for j in range(NA):
      line = file.readline();
      m = re.search(r"(?P<dh>\d{2}):(?P<dm>\d{2}) (?P<ah>\d{2}):(?P<am>\d{2})", line);
      dh = int(m.group("dh"));
      dm = int(m.group("dm"));
      ah = int(m.group("ah"));
      am = int(m.group("am"));
      trips_A.append( (dm+dh*60, am+ah*60) );

   for j in range(NB):
      line = file.readline();
      m = re.search(r"(?P<dh>\d{2}):(?P<dm>\d{2}) (?P<ah>\d{2}):(?P<am>\d{2})", line);
      dh = int(m.group("dh"));
      dm = int(m.group("dm"));
      ah = int(m.group("ah"));
      am = int(m.group("am"));
      trips_B.append( (dm+dh*60, am+ah*60) );

   trips_A.sort();
   trips_B.sort();
   nA, nB = schedule_trains(trips_A, trips_B, T);

   print "Case #" + str(i+1) + ": " + str(nA) + " " + str(nB);
