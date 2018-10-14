import copy
for case in range(input()):
    engines = []
    for engine in range(input()):
        engines.append(raw_input())
    engines_tmp = copy.copy(engines)
    switches = 0
    for line in range(input()):
        query = raw_input()
        if query in engines_tmp:
            if len(engines_tmp) > 1:
                engines_tmp.remove(query)
            else:
                engines_tmp = copy.copy(engines)                   
                engines_tmp.remove(query) 
                switches = switches + 1
    print 'Case #%s: %s' % (case + 1, str(switches))
