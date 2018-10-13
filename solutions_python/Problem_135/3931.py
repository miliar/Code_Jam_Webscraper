import sys
from Queue import Queue
import itertools
import pdb

def is_valid_line(line):
    try:
        if len( line ) != 4:
            print "Each row must have exactly 4 numbers."
            sys.exit(1)

        for i in line1:
            if (i < 1) or (i > 16):
                print "Invalid choice."
                sys.exit(1)
    except :
        print "Error."
        sys.exit(1)


if __name__ == '__main__':
    Q = Queue()
    try:
        T = int( raw_input() )
    except:
        print "Enter valid input number."
        sys.exit(1)

    count = 1
    while count <= int( T ):

        # first answer and matrix.
        try:
            ans1 = int( raw_input() )
        except:
            print "Enter valid answer."
            sys.exit(1)

        mat1 = []
        line1 = line2 = line3 = line4 = []
        line1 = raw_input()
        line1 = line1.split()
        line1 = [ int(i) for i in line1 ]
        is_valid_line( line1 )
        mat1.append( line1 )

        line2 = raw_input()
        line2 = line2.split()
        line2 = [ int(i) for i in line2 ]
        is_valid_line( line2 )
        mat1.append( line2 )

        line3 = raw_input()
        line3 = line3.split()
        line3 = [ int(i) for i in line3 ]
        is_valid_line( line3 )
        mat1.append( line3 )

        line4 = raw_input()
        line4 = line4.split()
        line4 = [ int(i) for i in line4 ]
        is_valid_line( line4 )
        mat1.append( line4 )

        ans_row1 = mat1[ ans1 - 1 ]



        # second answer and matrix.
        try:
            ans2 = int( raw_input() )
        except:
            print "Enter valid answer."
            sys.exit(1)

        mat2 = []
        line1 = line2 = line3 = line4 = []
        line1 = raw_input()
        line1 = line1.split()
        line1 = [ int(i) for i in line1 ]
        is_valid_line( line1 )
        mat2.append( line1 )

        line2 = raw_input()
        line2 = line2.split()
        line2 = [ int(i) for i in line2 ]
        is_valid_line( line2 )
        mat2.append( line2 )

        line3 = raw_input()
        line3 = line3.split()
        line3 = [ int(i) for i in line3 ]
        is_valid_line( line3 )
        mat2.append( line3 )

        line4 = raw_input()
        line4 = line4.split()
        line4 = [ int(i) for i in line4 ]
        is_valid_line( line4 )
        mat2.append( line4 )

        ans_row2 = mat2[ ans2 - 1 ]


        #pdb.set_trace()

        # main logic.


        if len( set.intersection( set(ans_row1), set(ans_row2) )) == 1:
            ans = list( set.intersection( set(ans_row1), set(ans_row2) ) )[0]
            print "Case #%s: %s"%(count, ans)
        if len( set.intersection( set(ans_row1), set(ans_row2) )) > 1:
            print "Case #%s: Bad magician!"%(count)
        if len( set.intersection( set(ans_row1), set(ans_row2) )) == 0:
            print "Case #%s: Volunteer cheated!"%(count)

        """


        status = 0
        for line in mat2:
            if not len( set.intersection( set(line), set(ans_row1) ) ) == 1:
                status = 1

        if status == 0:
            ans  = int( list(set.intersection(set(ans_row1), set(ans_row2)))[0] )
            print "Case #%s: %s"%(count, ans)

        if status == 1:
            cnt = 0
            '''
            for i in mat1:
                if i in mat2:
                    cnt += 1

            if cnt == 0:
                print "Case #%s: Volunteer cheated!"%(count)
            else:
            '''
            if ans1 != ans2:
                print "Case #%s: Volunteer cheated!"%(count)
            else:
                print "Case #%s: Bad magician!"%(count)

        """

        count += 1
