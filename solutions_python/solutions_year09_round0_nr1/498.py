L, D, N = [int(x) for x in raw_input().split() ]

#print L, D, N

word_list = []
index_list = [ dict() for _ in xrange(L) ]
for i in xrange(D):
    word_list.append( raw_input() )
    char_list = list(word_list[i])
    #print char_list
    new_index = dict()
    for char_pos in xrange(L):
        if index_list[char_pos].has_key( char_list[char_pos] ):
            index_list[char_pos][ char_list[char_pos] ].append(i)
        else:
            index_list[char_pos][ char_list[char_pos] ] = [i]

#print index_list
#quit()

#The pattenrns
for pattern_count in xrange(N):
    pattern = list(raw_input())
    #print pattern
    part_list = []
    i = 0
    i_max  = len(pattern)
    while i < i_max:
        part = []
        if pattern[i] == "(":
            i += 1
            #read until )
            while pattern[i] != ")": 
                part.append( pattern[i] )
                i += 1

            i += 1
        else:
            part.append( pattern[i] )
            i += 1

        #print part
        part_list.append(part)

    #Math logic
    #print part_list
    match_word_list = []
    if len( part_list ) == L:

        def words_for( char_list, pos ):
            global index_list
            result = []
            for c in char_list:
                if index_list[pos].has_key(c):
                    result.extend(index_list[pos][c])
            return result
            

        #match list starts with the first words
        match_list = words_for( part_list[0], 0 )

        for part_count in xrange(1,L):
            next_list = []
            candidate_list = words_for( part_list[part_count], part_count )
            for w in candidate_list:
                if w in match_list:
                    next_list.append(w)

            match_list = next_list

        print "Case #%d: %d" % (pattern_count+1, len(match_list))
    else:
        print "Case #%d: %d" % (pattern_count+1, 0)

# print word_list



