if __name__ == '__main__':
    f = open('A-large.in', 'r')
    o = open('A-large.out', 'w')

    T = int(f.readline().strip())
    
    for i in range(1, T + 1):
        line = f.readline().strip().split()
        Smax = int(line[0])
        S = line[1]
        
        already_standing = 0
        extra_friends_total = 0
        
        for shyness_level in range(Smax + 1) :
            extra_friends = 0
            if shyness_level > already_standing:
                extra_friends += shyness_level - already_standing
            already_standing += int(S[shyness_level]) + extra_friends
            extra_friends_total += extra_friends
        
        o.write('Case #' + str(i) + ': ' + str(extra_friends_total)+'\n')
