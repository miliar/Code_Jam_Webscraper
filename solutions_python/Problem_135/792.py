# Written by python version 3

def get_cases():
    import sys

    with open( sys.argv[ -1 ], "r" ) as data:
        lines = [ line.rstrip().split() for line in data ]
        lines = lines[ 1 : ]

    cases = [ lines[ index * 10 : index * 10 + 10 ]\
    for index, line in enumerate( lines[ : : 10 ] ) ]

    return cases

def get_result( case ):
    ans_1 = int( case[ 0 ][ 0 ] )
    ans_2 = int( case[ 5 ][ 0 ] )

    memory = {}

    for item in case[ ans_1 ]:
        memory[ item ] = 1

    indicator = 0
    value = 0
    for item in case[ ans_2 + 5 ]:
        if item in memory.keys():
            value = item
            indicator += 1

    if indicator == 0:
        return "Volunteer cheated!"

    elif indicator == 1:
        return value

    else:
        return "Bad magician!"

cases = get_cases()

for index, case in enumerate( cases ):
    print( "Case #{0}: {1}".format( index + 1, get_result( case ) ) )
