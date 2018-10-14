def findFreq(notes, lowest, highest):
    for note in range(lowest, highest+1):
        note_in_harmony = True
        for other_note in notes:
            if other_note%note != 0 and note%other_note != 0:
                note_in_harmony = False
                break
        if note_in_harmony:
            return note
    return None

for case in xrange(input()):
    vars = raw_input().split()
    
    num_players = int(vars[0])
    lowest_note = int(vars[1])
    highest_note = int(vars[2])
    
    played_notes_inp = raw_input().split()
    
    played_notes = []
    
    for played_note in played_notes_inp:
        played_notes.append(int(played_note))
        
    res = findFreq(played_notes, lowest_note, highest_note)

    if not res:
        print "Case #%i: NO" % (case+1)
    else:
        print "Case #%i: %i" % (case+1, res)
