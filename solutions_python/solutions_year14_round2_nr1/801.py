
from math import ceil, floor
IMPOSSIBLE = "Fegla Won" 

def solve(N,words):

    # Extract profile from first word.
    profile = words[0][0]
    for i in xrange(1,len(words[0])):
        if words[0][i-1] != words[0][i]:
            profile += words[0][i]
    # Profile is done.

    # The answer.
    total_operations = 0
    
    positions = N*[0]
    
    # For each letter in the profile, compute
    # the cardinal for each given word.
    for letter in profile:

        letter_in_word = N*[0]
        
        for i in xrange(len(words)):

            if positions[i] == len(words[i]) or words[i][positions[i]] != letter:
                return IMPOSSIBLE

            while positions[i] < len(words[i]) and words[i][positions[i]] == letter:
                letter_in_word[i] += 1
                positions[i] += 1

        # We know the letter count in every word. Compute the average:
        average = sum(letter_in_word)/float(N)
        up = int(ceil(average))
        down = int(floor(average))

        operations = min( sum( int(abs(letter_in_word[i] - avg)) for i in xrange(N) ) for avg in (up,down) )
        total_operations += operations

    if sum(positions) == sum(len(word) for word in words):
        return total_operations
    else:
        return IMPOSSIBLE    

    
if __name__ == '__main__':

    T = int(raw_input())

    for t in xrange(1,T+1):
        N = int(raw_input())
        words = [ raw_input() for _ in xrange(N) ]
        print "Case #%d: %s" % (t, solve(N,words) )
    
