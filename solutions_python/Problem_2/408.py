#! /usr/bin/python
import sys

def get_raw(time):
   hour = int(time.split(':')[0])
   min = int(time.split(':')[1])
   raw = hour * 60 + min
   return raw

def sooner_arrival(pair1, pair2):
   """
   Returns < 0 if pair 1 has a sooner arrival
   """
   return pair1[1] - pair2[1]


inf = open(sys.argv[1],'r').readlines()
inf_line = 0
n = int(inf[inf_line])
inf_line += 1
output = ''
for case in range(n):
   t_time = int(inf[inf_line])
   inf_line += 1
   NA = int(inf[inf_line].split(' ')[0])
   NB = int(inf[inf_line].split(' ')[1])
   inf_line += 1

   NA_sched = []
   NA_sched_pretty = []
   for i in range(NA):
      depart_raw = get_raw( inf[inf_line].split(' ')[0] )
      arrive_raw = get_raw( inf[inf_line].split(' ')[1] )
      NA_sched.append((depart_raw,arrive_raw))
      NA_sched_pretty.append(inf[inf_line].strip())
      inf_line += 1

   NB_sched = []
   NB_sched_pretty = []
   for i in range(NB):
      depart_raw = get_raw( inf[inf_line].split(' ')[0] )
      arrive_raw = get_raw( inf[inf_line].split(' ')[1] )
      NB_sched.append((depart_raw,arrive_raw))
      NB_sched_pretty.append(inf[inf_line].strip())
      inf_line += 1

   NA_sched.sort(sooner_arrival)
   NB_sched.sort(sooner_arrival)

#  print 't_time', t_time
#  print 'NA_sched:', NA_sched
#  print 'NB_sched:', NB_sched

   trip = 0 # number of trips figured out
   a_trains = [] # trains currently on side A (value = time they are ready)
   b_trains = [] # trains currently on side B (value = time they are ready)
   a_start = 0 # number of trains that will start on side A
   b_start = 0 # number of trains that will start on side B
   while trip < NA+NB:
      trip += 1
      a_trains.sort() # so that earliest ready time is at idx 0
      b_trains.sort() # so that earliest ready time is at idx 0
      if NA_sched and NB_sched:
         if sooner_arrival(NA_sched[0], NB_sched[0]) < 0:
            sched_to_take = 'a'
         else:
            sched_to_take = 'b'
      elif NA_sched:
            sched_to_take = 'a'
      else: # only NB_sched left
            sched_to_take = 'b'

      if sched_to_take == 'a':
         # take the A sched
         depart,arrive = NA_sched.pop(0)
         if (a_trains and a_trains[0] <= depart):
            a_trains.pop(0)
         else:
            a_start += 1
         b_trains.append(arrive + t_time)
      else:
         # take the B sched
         depart,arrive = NB_sched.pop(0)
         if (b_trains and b_trains[0] <= depart):
            b_trains.pop(0)
         else:
            b_start += 1
         a_trains.append(arrive + t_time)

   assert not NA_sched and not NB_sched
   answer = "Case #%d: %d %d\n" % (case+1, a_start, b_start)
#  print answer
   output += answer
   
outf = open(sys.argv[2],'w')
outf.write(output)
outf.close()


