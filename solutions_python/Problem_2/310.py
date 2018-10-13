#!/usr/bin/env python

# using datetime module to make the arithmetic of arrival/departure times
# and turnaround times easy. 
import datetime


class CTrain:
    def __init__(self, tm):
        self.time = tm # Time of arrival or departure
        self.scheduled = False # if the train has already been scheduled for departure
        
    def reset(self):
        self.scheduled = False
    
class CEntry2:
    def __init__(self, dep, arr):
        self.arr = arr
        self.dep = dep
        
    def __str__(self):
        return 'dep: %s : arr: %s' % (str(self.dep), str(self.arr))
        
    
def GetDateTime( train_time ):
    ''' The input is time in format '10:30', '12:02' etc.
        The function returns a date time object with the time
        passed in the format indicated above'''
        
    train_time = train_time.strip()
    
    
    
    times = [x.strip() for x in train_time.split(':')]
    #print times
    
    if times[0][0] == '0':
        times[0] = times[0][1:]
    if times[1][0] == '0':
        times[1] = times[1][1:]
    
    #print times
    times = [eval(x) for x in times ]
    
    # Here the date does not matter. But the date time module
    # requires the date, month and year to be passed. So, passing
    # today's date. 
    return datetime.datetime( 2008, 7, 17, hour = times[0], minute = times[1] )
        


def process_one_input( input):
    l = input.split( '\n' )
    
    # First line gives the round trip time (T)
    T = datetime.timedelta( minutes = eval(l[0]) )
    
    num_trips = [ eval(x) for x in l[1].strip().split() ]

    # The first element of line 2 gives the num trips from A to B
    # and the second element gives the num trips from B to A
    num_trips_a = num_trips[ 0 ]
    num_trips_b = num_trips[ 1 ]
    
    A_Dep = []
    A_Arr = []
    
    B_Dep = []
    B_Arr = []
    
    k = []
    for i in range( 2, 2 + num_trips_a):
        k.append( CEntry2( GetDateTime(l[i].split()[0].strip()),
                           GetDateTime(l[i].split()[1].strip()) ))
        
    def cmp(x,y):
        if x.dep < y.dep: return -1
        if x.dep > y.dep: return 1
        return 0
    
    k.sort( cmp )
        
    for j in k:
        #print j
        A_Dep.append( CTrain( j.dep ) )
        B_Arr.append( CTrain( j.arr ) )
        
    
    k = []
    for i in range( 2 + num_trips_a, 2 + num_trips_a + num_trips_b ):
        k.append( CEntry2( GetDateTime(l[i].split()[0].strip()),
                           GetDateTime(l[i].split()[1].strip()) ))

    k.sort( cmp )
    
    for j in k:
        #print j
        B_Dep.append( CTrain( j.dep ) )
        A_Arr.append( CTrain( j.arr ) )
        
    return A_Dep, B_Arr, B_Dep, A_Arr, T


def train_count(dep, arr, T):
    train_count = 0 #len(dep)
    
    [ x.reset() for x in dep ]
    [ x.reset() for x in arr ]
    
    for i in dep:
        
        # we can schedule a train for departure if the arrival time
        # + the turnaround time < departure time
        #
        # However, if a train has been scheduled already for departure
        # we shouldnt count it again for the next departure (since the
        # train would have left already)
        
        may_schedule = [ x for x in arr if (x.time + T) <= i.time ]
        
        #print may_schedule, arr, i
        reschedule = False
        for j in may_schedule:
            if j.scheduled == False: 
                #train_count -= 1
                j.scheduled = True
                reschedule = True
                break # from inner 'j' loop
        
        
        if reschedule == False:
            train_count += 1
            

    return train_count



def main():
    l = open('B-large.in').readlines()
    num_inputs = eval(l[0].strip())
    lc = 0
    
    for i in range(num_inputs):
        lc += 1
        input = l[lc]
        
        lc += 1
        input += l[lc]
        num_lines = sum( [eval(x.strip()) for x in l[lc].split()])
        
        for j in range(num_lines):
            lc += 1
            input += l[lc]

        # 'input' now has one set of data i.e one test case
        A_Dep, B_Arr, B_Dep, A_Arr, T = process_one_input( input )
        
        '''
        for i in range(len(A_Dep)):
            print A_Dep[i].time, B_Arr[i].time

        for i in range(len(B_Dep)):
            print B_Dep[i].time, A_Arr[i].time'''
            

            
        print 'Case #%d: %d %d' % ( i+1, train_count( A_Dep, A_Arr, T ),  train_count( B_Dep, B_Arr, T ))
        #print
        

        
        
        
if __name__ == '__main__':
    main()
    