class timex:

    def __init__( self, hours, mins ):
        self.hours = hours
        self.mins = mins
        self.timestamp = hours * 60 + mins

    def __add__( t0, mins ):
        t = timex( t0.hours, t0.mins )
        t.timestamp += mins
        t.hours = t.timestamp / 60
        t.mins = t.timestamp % 60
        return t
    def __repr__( self ):
        return "%d:%d"%(self.hours,self.mins)

def timex_from_str( s ):
    t = s.split(':')
    return timex( int(t[0]), int(t[1] ) )


def cmp_events( a, b ):

    if a[0].timestamp == b[0].timestamp:
        if a[1].startswith( 'ready' ):
            return -1
        elif b[1].startswith( 'ready' ):
            return 1
        return 0

    if a[0].timestamp < b[0].timestamp:
        return -1

    return 1

def main( fn ):
    f = open( fn, 'rt' )
    N = int( f.readline() )

    for case in range( 0, N ):
        T = int( f.readline() )
        s = f.readline().split()
        NA = int(s[0])
        NB = int(s[1])

        timeline = []

        for trip in range( 0, NA ):
            s = f.readline().split()

            departure = timex_from_str( s[0] )
            arrival = timex_from_str( s[1] )

            timeline.append( (departure,'departure a') )

            ready = arrival + T
            timeline.append( (ready,'ready b') )

        for trip in range( 0, NB ):
            s = f.readline().split()

            departure = timex_from_str( s[0] )
            arrival = timex_from_str( s[1] )

            timeline.append( (departure,'departure b') )

            ready = arrival + T
            timeline.append( (ready,'ready a') )

        timeline.sort( cmp = cmp_events )

        trains_in_a = 0 # trains currenly in A
        trains_in_b = 0 # trains currenly in B

        a_trains_req= 0 # answer
        b_trains_req= 0 # answer

        for event in timeline:

            if event[1] == 'departure a':
                if trains_in_a == 0:
                    a_trains_req+= 1
                else:
                    trains_in_a -= 1

            elif event[1] == 'departure b':
                if trains_in_b == 0:
                    b_trains_req+= 1
                else:
                    trains_in_b -= 1

            elif event[1] == 'ready a':
                trains_in_a += 1

            elif event[1] == 'ready b':
                trains_in_b += 1
            else:
                print 'unknown event: ', event[1]
            #print event, 'A: ', trains_in_a, 'B: ', trains_in_b, 'Areq: ', a_trains_req, 'Breq: ', b_trains_req

            


        print 'Case #%d: %d %d'%(case+1, a_trains_req, b_trains_req )

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        main( sys.argv[1] )
    else:
        print 'use filename'


