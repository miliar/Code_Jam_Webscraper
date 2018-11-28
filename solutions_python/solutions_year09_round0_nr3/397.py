#import psyco
#psyco.full()

welcome_list = list("welcome to code jam")
wel_len = len(welcome_list)
unique_list = list("welcom tdja" )
for test_case in xrange(input()):
    text_list = list(raw_input())
    letter_map = dict()
    for l in unique_list:
        letter_map[l] = []
    pos = 0
    for l in text_list:
        if l in unique_list:
            letter_map[l].append(pos)

        pos += 1

    wel_len_list = [ 0 for _ in range(wel_len)]
    idx = 0
    pos_list = []
    def do_pos(start, wel_pos):
        global welcome_list
        if wel_pos == wel_len:
            return 1

        l = [ x for x in letter_map[welcome_list[wel_pos]] if x > start]
        if len(l) == 0: return 0

        result = 0
        for p in l:
            local = do_pos(p,wel_pos+1)
            if local > 0:
                result += local
            #else:
            #    return 0

        return result

    result = 0
    l = letter_map[welcome_list[0]]
    for p in l:
        result += do_pos(p, 1)

    print "Case #%d: %.4d" %( test_case+1, result )

        


        
    


