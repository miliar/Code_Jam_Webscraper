def invokeElements(to_invoke, combine_pairs, opposed_elements):
    element_list = []
    
    for element in to_invoke:
        if len(element_list) == 0:
            element_list.append(element)
        else:
            latest_pair = "%s%s" % (element_list[-1], element)
            if combine_pairs.has_key(latest_pair):
                element_list.pop()
                element_list.append(combine_pairs[latest_pair])
            else:
                element_list.append(element)
            
            #check for opposed_elements
            for opposed in opposed_elements:
                if opposed[0] in element_list and opposed[1] in element_list:
                    element_list = []
                
    return element_list

for case in xrange(input()):
    input = raw_input().split()
    
    combine_pairs = {}
    opposed_elements = []
    to_invoke = []
    
    num_combine_pairs = int(input[0])
    
    if num_combine_pairs > 0:
        combine_pairs_inp = input[1:num_combine_pairs + 1]
        for combine_pair in combine_pairs_inp:
            new_element = combine_pair[2]
            combine_pairs["%s%s" % (combine_pair[0], combine_pair[1])] = new_element
            combine_pairs["%s%s" % (combine_pair[1], combine_pair[0])] = new_element

    num_opposed_elements = int(input[num_combine_pairs + 1])
    
    if num_opposed_elements > 0:
        opposed_elements_inp = input[num_combine_pairs + 2:num_combine_pairs + num_opposed_elements + 2]
        for opposed_element in opposed_elements_inp:
            opposed_elements.append([opposed_element[0], opposed_element[1]])
    
    num_to_invoke = int(input[num_combine_pairs + 1 + num_opposed_elements + 1])
    letters_to_invoke = input[-1]
    for invoke in range(num_to_invoke):
        to_invoke.append(letters_to_invoke[invoke])
    
    res = invokeElements(to_invoke, combine_pairs, opposed_elements)

    s = ", ".join(res)

    print "Case #%i: [%s]" % (case+1, s)