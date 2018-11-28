for case in xrange(1, input() + 1):
    num_existing, num_tobe = [int(x) for x in raw_input().split()]
    existing = [raw_input() for x in xrange(num_existing)]
    tobe = [raw_input() for x in xrange(num_tobe)]
    num_mkd = 0
    for i in xrange(num_tobe):
        biggest_string = '/'
        for j, string in enumerate(existing):
            if  len(string) <= len(tobe[0]) and tobe[0][:len(string)] == string and len(biggest_string) <= len(string):
                biggest_string = string
        string = tobe[0]
        while biggest_string != string:
           if biggest_string != '/':
               biggest_string = biggest_string + '/'
           some_loc  = string[len(biggest_string):].find('/')
           if some_loc == -1:
               existing.append(string)
               num_mkd += 1
               biggest_string = string
           else:
               existing.append(string[:len(biggest_string) + some_loc])
               num_mkd += 1
               biggest_string = string[:len(biggest_string) + some_loc] 
        tobe.pop(0)
    print 'Case #' + str(case) + ':',  num_mkd
