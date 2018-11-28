import sys

input = sys.stdin
cases = int(input.readline())

for case in xrange (cases):
    line = input.readline().strip().split(" ")
    
    total_combines = int(line[0])
    list_mark = 1 + total_combines
    combines = line[1:list_mark]
    
    total_opposed = int(line[list_mark])
    opposed = line[list_mark+1:list_mark+1+total_opposed]
    
    opposed_sets = []
    for o in opposed:
        opposed_sets.append(set([o[0], o[1]]))
    
    list_mark = list_mark+1+total_opposed
    
    total_chars = int(line[list_mark])
    chars = line[list_mark+1]

    combine_translation = dict()
    for combine in combines:
        base = combine[0:2]
        nonbase = combine[2]
        
        combine_translation[base] = nonbase
        combine_translation[base[::-1]] = nonbase

    element_list = []
    for i in range(total_chars):
        element_list.append(chars[i])
        size = len(element_list)
        if  size >= 2:
            translation = combine_translation.get("".join(element_list[size-2:]))
            if not translation is None:
                element_list.pop()
                element_list.pop()
                element_list.append(translation)

        # opposed
        element_list_set = set(element_list)
        for o in opposed_sets:
            
            if (element_list_set.intersection(o) == o):
                element_list = []
                
    print "Case #%d: [%s]" % (case + 1, ", ".join(element_list))
