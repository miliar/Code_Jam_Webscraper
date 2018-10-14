def resolve(stack, translation_dict, clearings):
    while tuple(stack[-2:]) in translation_dict:
        stack = stack[:-2] + [translation_dict[tuple(stack[-2:])]]
        
    for clearing in clearings:
        if (clearing[0] in stack) and (clearing[1] in stack):
            stack = []
            
    return stack

def process(s):
    original_line = split_line = s.split(' ')
    
    number_of_translations, split_line = int(split_line[0]), split_line[1:]
    translations, split_line = split_line[:number_of_translations], split_line[number_of_translations:]
    
    number_of_clearings, split_line = int(split_line[0]), split_line[1:]
    clearings, split_line = split_line[:number_of_clearings], split_line[number_of_clearings:]
    
    number_of_elements, spell = int(split_line[0]), split_line[1]
    
    translation_dict = {}
    
    for translation in translations:
        translation_dict[tuple(translation[0] + translation[1])] = translation[2]
        translation_dict[tuple(translation[1] + translation[0])] = translation[2]
    
    stack = []
    
    for elem in spell:
        stack.append(elem)
        stack = resolve(stack, translation_dict, clearings)
        
    return '[' + ', '.join(stack) + ']'
    
number_of_cases = int(raw_input())
for case_number in xrange(1, number_of_cases+1):
    s = raw_input()
    
    result = process(s)

    print "Case #%d: %s" % (case_number, result)
    case_number += 1