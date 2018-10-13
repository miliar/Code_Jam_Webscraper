#!/usr/bin/python
import sys
import copy

szfile = './B-large.in.txt'
szfile_output = './B-large.output.txt'
##szfile = 'B-small-attempt0.in.txt'
##szfile_output = './B-small.output.txt'

class TrainTimetable:
    def __init__(self):
        pass

    def RunFile(self) :
# using file set
        f = open(szfile,'rb')
# ---
        ncase = int(f.readline())

        l_output = []
        for i in xrange(ncase):
            T = int(f.readline())
            szline = f.readline()
            l_line = szline.split()
            na = int(l_line[0]); nb = int(l_line[1])
            NA = []; NB = []
            for x in xrange(na):
                NA.append(f.readline())
            for x in xrange(nb):
                NB.append(f.readline())

            mina, minb = self.GetMinTrain(NA, NB, T)
            num = i + 1
            l_output.append('Case #%(num)d: %(mina)d %(minb)d' %locals())
# using file set
        f = open(szfile_output,'wb')
        f.write('\n'.join(l_output))
# ----


    def GetMinTrain(self, NA, NB, T):
        DA = []     #tutple list
        DB = []
        for x in NA:
            szst, szed = x.split(' ', 1)
            nst = self.GetMinute(szst)
            ned = self.GetMinute(szed)
            DA.append([nst, ned, False, False])     #st, ed, link_out, link_in
        for x in NB:
            szst, szed = x.split(' ', 1)
            nst = self.GetMinute(szst)
            ned = self.GetMinute(szed)
            DB.append([nst, ned, False, False])
        DA.sort(); DB.sort()
##        print DA
##        print DB

        #finding link B->A
        for i, x in enumerate(DA):
            maxarv = -1;
            maxnd = -1;
            for j, y in enumerate(DB):
                if(y[1]+T <= x[0] and y[2] == False) :
                    if(maxarv < y[1]+T):
                        maxarv = y[1]+T
                        maxnd = j
            if(maxnd != -1):
                DB[maxnd][2] = True
                DA[i][3] = True

##        print
##        print DA
##        print DB
        #finding link A->B
        for i, x in enumerate(DB):
            maxarv = -1;
            maxnd = -1;
            for j, y in enumerate(DA):
                if(y[1]+T <= x[0] and y[2] == False) :
                    if(maxarv < y[1]+T):
                        maxarv = y[1]+T
                        maxnd = j
            if(maxnd != -1):
                DA[maxnd][2] = True
                DB[i][3] = True

##        print
##        print DA
##        print DB

        sta = 0; stb = 0
        for x in DA:
            if(x[3] == False):
                sta += 1
        for x in DB:
            if(x[3] == False):
                stb += 1

        return (sta, stb)

    def GetMinute(self, sztime):
        l_time = sztime.split(':')
        nhour = int(l_time[0])
        nmin = int(l_time[1])
        return nhour*60+nmin


if __name__ == "__main__":
    cm = TrainTimetable()
##    print cm.GetMinTrain(['09:00 12:00', '10:00 13:00', '11:00 12:30',], ['12:02 15:00', '09:00 10:30',], 5)
##    print cm.GetMinTrain(['09:00 09:01', '12:00 12:02',], [], 2)
    cm.RunFile()

