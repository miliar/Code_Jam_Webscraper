import sys

def strip_lines( lines ):
    result = []
    for line in lines:
        result.append( line.strip() )
    return result

def get_cases( lines ):
    cases = []
    case = []
    for line in lines:
        if line == "":
            cases.append( case )
            case = []
        else:
            case.append( line )
    return cases

def check_finished( case ):
    for line in case:
        if "." in line:
            return False
    return True

def check_result( case ):
    def check_string( string ):
        if "." in string:
            return "No result"
        else:
            if "X" in string and "O" not in string:
                return "X won"
            elif "O" in string and "X" not in string:
                return "O won"
            else:
                return "No result"
    # Check rows
    result_1 = check_string( case[ 0 ] )
    result_2 = check_string( case[ 1 ] )
    result_3 = check_string( case[ 2 ] )
    result_4 = check_string( case[ 3 ] )
    # Check columns
    result_5 = check_string( case[ 0 ][ 0 ] + case[ 1 ][ 0 ] + case[ 2 ][ 0 ] + case[ 3 ][ 0 ] )
    result_6 = check_string( case[ 0 ][ 1 ] + case[ 1 ][ 1 ] + case[ 2 ][ 1 ] + case[ 3 ][ 1 ] )
    result_7 = check_string( case[ 0 ][ 2 ] + case[ 1 ][ 2 ] + case[ 2 ][ 2 ] + case[ 3 ][ 2 ] )
    result_8 = check_string( case[ 0 ][ 3 ] + case[ 1 ][ 3 ] + case[ 2 ][ 3 ] + case[ 3 ][ 3 ] )
    # Check diagonals
    result_9 = check_string( case[ 0 ][ 0 ] + case[ 1 ][ 1 ] + case[ 2 ][ 2 ] + case[ 3 ][ 3 ] )
    result_10 = check_string( case[ 0 ][ 3 ] + case[ 1 ][ 2 ] + case[ 2 ][ 1 ] + case[ 3 ][ 0 ] )
    #--------------------------------------------------------------------------------------------
    if result_1 != "No result":
        return result_1
    elif result_2 != "No result":
        return result_2
    elif result_3 != "No result":
        return result_3
    elif result_4 != "No result":
        return result_4
    elif result_5 != "No result":
        return result_5
    elif result_6 != "No result":
        return result_6
    elif result_7 != "No result":
        return result_7
    elif result_8 != "No result":
        return result_8
    elif result_9 != "No result":
        return result_9
    elif result_10 != "No result":
        return result_10
    else:
        if check_finished( case ) == True:
            return "Draw"
        else:
            return "Game has not completed"

lines = []
with open( sys.argv[ -1 ], "r" ) as f_in:
    lines = f_in.readlines()
    lines = strip_lines( lines[ 1: ] )

cases = get_cases( lines )

for index, case in enumerate( cases ):
    print "Case #{0}: {1}".format( index + 1, check_result( case ) )
