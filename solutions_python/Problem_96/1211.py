# dancing.vim -- find the maximum number of people with scores of the specified amount

num_cases = int ( input() )
current_case = 0

while ( current_case < num_cases ) :
    num_above = 0
    line = input()
    total_scores = line.split( ' ' )
    for x in range( len( total_scores ) ) :
        total_scores[x] = int( total_scores[x] )

    num_people = total_scores.pop(0)
    num_surprising = total_scores.pop(0)
    at_least = total_scores.pop(0)

    while ( len( total_scores ) > 0 ) :
        current_test = total_scores.pop( 0 ) - at_least # the remainding 2 values
        not_surprising_min = ( 2 * ( at_least - 1 ) )
        surprising_min = ( 2 * ( at_least - 2 ) )
        if surprising_min < 0 :
            surprising_min = 0

        if current_test >= not_surprising_min :
            num_above += 1
        elif ( current_test >= surprising_min ) and ( num_surprising > 0 ) :
            num_above += 1
            num_surprising -= 1
    
    current_case += 1

    print( "Case #", current_case, ": ", num_above, sep = '' )
