

f = open('input', 'r')


no_test_cases = int(f.readline())


for i in range( 0 , no_test_cases):
    first_answer = int(f.readline())
    first_rows = []
    for j in range( 0 ,4 ):
        first_rows.append( map(int, f.readline().split()))
                            

    second_answer = int(f.readline())
    second_rows = []
    for j in range( 0 ,4 ):
        second_rows.append( map(int, f.readline().split()))

    first_answer -=1
    second_answer -=1
    options = []
    for r in first_rows[first_answer]:
        if r in second_rows[second_answer]:
            options.append( r)
    print "Case #" + str(i+1) +": ",


    if len(options) == 1:
        print options[0]
    elif len(options) == 0:
        print "Volunteer cheated!"
    else:
        print "Bad magician!"


    
        
    
