#!/usr/bin/env python


from sys import argv
from datetime import datetime, timedelta



class Schedule():
    def __init__(self, sched):
        #self.end_of_journey  = time(23, 59)
        self._init_sched(sched)

    def __ge__(self, y):
        t1 = self._ls[0][0]
        t2 = y._ls[0][0]
        if t1 >= t2:
            return True
        else:
            return False

    def __getitem__(self, i):
        return self._ls[i]
        
    def __gt__(self, y):
        t1 = self._ls[0][0]
        t2 = y._ls[0][0]
        if t1 > t2:
            return True
        else:
            return False

    def __le__(self, y):
        t1 = self._ls[0][0]
        t2 = y._ls[0][0]
        if t1 <= t2:
            return True
        else:
            return False

    def __lt__(self, y):
        t1 = self._ls[0][0]
        t2 = y._ls[0][0]
        if t1 < t2:
            return True
        else:
            return False

    def __len__(self):
        return len(self._ls)

    def _init_sched(self, sched):
        """_ls: list of departure, arrival times. reserve: list of departure times for foreign trains"""
        self._ls = []
        for  row in sched:
            time_dep, time_arrival = [self._timeobj(i) for  i in row]
            self._ls.append((time_dep, time_arrival))
        self._ls.sort()
        self.reserve = []
            
    def _timeobj(self, arg):
        hh, mm = arg.split(":")
        return datetime(2008, 7, 17, int(hh), int(mm))

    def get_schedule(self):
        return self._ls
    
    def get_schedule_with_delta(self, timedelta):
        __ls = []
        for row  in self._ls:
            time_dep, time_arrival = row
            self.__ls.append((time_dep, time_arrival + timedelta))
        return __ls
    
    def add_to_reserve(self, t):
        self.reserve.append(t)

    def pop(self, pos):
        return self._ls.pop(pos)
    


class TrainStation():
    def __init__(self, delay, schedA, schedB):
        self.delay = timedelta(minutes = delay)
        self.sched_A = Schedule(schedA)
        self.res_A = self.sched_A.reserve
        self.sched_B = Schedule(schedB)
        self.res_B = self.sched_B.reserve        
        self._init_stations()
        if not self.stop:
            self.populate_stations()


    def _init_stations(self):
        self.trains_A = 0
        self.trains_B = 0
        self.stop = False

        if len(self.sched_A) == 0:
            self.trains_B = len(self.sched_B)
            self.trains_A = 0
            self.stop = True
            
        elif len(self.sched_B) == 0:
            self.trains_A = len(self.sched_A)
            self.trains_B = 0
            self.stop = True
            
        
    def populate_stations(self):
        len_A = len(self.sched_A)
        len_B = len(self.sched_B)
        
        if len_A == 0 and len_B == 0:
            return

        elif len_A == 0:
            while len(self.sched_B) > 0:
                dep_time, arrival_time = self.sched_B.pop(0)
                if self.res_B != []:
                    if self.res_B[0] <= dep_time:
                        self.res_B.pop(0)
                    else:
                        self.trains_B += 1
                else:
                    self.trains_B += 1
            return

        elif len_B == 0:
            while len(self.sched_A) > 0:
                dep_time, arrival_time = self.sched_A.pop(0)
                if self.res_A != []:
                    if self.res_A[0] <= dep_time:
                        self.res_A.pop(0)
                    else:
                        self.trains_A += 1
                else:
                    self.trains_A += 1
            return

        elif self.sched_A <= self.sched_B:
            dep_time, arrival_time = self.sched_A[0]
            if self.res_A == []:
                self.trains_A += 1
#                self.sched_A.pop(0)
#                self.res_B.append(arrival_time + self.delay)
#                self.res_B.sort()
            else:
                if self.res_A[0] <= dep_time:
                    self.res_A.pop(0)
#                    self.sched_A.pop(0)
#                    self.res_B.append(arrival_time + self.delay)
#                    self.res_B.sort()
                else:
                    self.trains_A += 1
#                    self.sched_A.pop(0)
#                    self.res_B.append(arrival_time + self.delay)
#                    self.res_B.sort()
            self.sched_A.pop(0)
            self.res_B.append(arrival_time + self.delay)
            self.res_B.sort()
            self.populate_stations()
            
        elif self.sched_A > self.sched_B:
            dep_time, arrival_time = self.sched_B[0]
            if self.res_B == []:
                self.trains_B += 1

            else:
                if self.res_B[0] <= dep_time:
                    self.res_B.pop(0)

                else:
                    self.trains_B += 1
            self.sched_B.pop(0)
            self.res_A.append(arrival_time + self.delay)
            self.res_A.sort()
            self.populate_stations()
                
        else:
            print "something bad happened!. You should not be here!!!"
            


fd = open(argv[1])
N  = int(fd.readline())
for  k in range(N):
    T = int(fd.readline())
    NA, NB = [int(i) for i in fd.readline().split()]
    schedule_A = []
    schedule_B = []
    for i in range(NA):
        dep_time, arrival_time = fd.readline().split()
        schedule_A.append((dep_time, arrival_time))
    for i in range(NB):
        dep_time, arrival_time = fd.readline().split()
        schedule_B.append((dep_time, arrival_time))
    
    train_admin = TrainStation(T, schedule_A, schedule_B)
    print "Case #%i: %i %i" %(k + 1, train_admin.trains_A, train_admin.trains_B)
#    print T, NA, NB, schedule_A, schedule_B
