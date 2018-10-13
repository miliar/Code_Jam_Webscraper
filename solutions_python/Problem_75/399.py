import re
import sys

if not len(sys.argv) == 3:
    exit("""Wrong usage parameters supplied!
    
    Usage:
    %s input output""" % __file__
    )

BASE_ELEMS = "QWERASDF"

def extract_rules(s):
    (rules_count, s) = s.split(" ", 1)
    rules = []
    rules_count = int(rules_count)
    if int(rules_count):
        rules_parts = s.split(" ", rules_count)
        (rules, s) = (rules_parts[0:rules_count], rules_parts[rules_count])
    return (rules, s)

def get_sorted_seq(el1, el2):
    return "%s%s" %\
        ((el1, el2) if el1 < el2 else (el2, el1))

def get_resulting_elems_list(seq, combine_rules, opposed_rules):
    
    elems_list = []
    
    for el in seq:
        
        elems_list.append(el)
        
        if (len(elems_list) < 2):
            continue
        
        last_pair_elems = elems_list[-2:]
        last_pair = get_sorted_seq(last_pair_elems[0], last_pair_elems[1])
        if last_pair in combine_rules:
            elems_list = elems_list[:-2] + [combine_rules[last_pair]]
        else:
            for pair_elem in elems_list[:-1]:
                if (pair_elem in BASE_ELEMS) and (get_sorted_seq(el, pair_elem) in opposed_rules):
                    elems_list = []
                    break
    
    return elems_list

def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    output_f = open(output_filename, "w")
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):
            s = input_f.readline().strip()
            
            combine_rules = {}
            (raw_combine_rules, s) = extract_rules(s)
            for raw_combine_rule in raw_combine_rules:
                combine_rules[get_sorted_seq(raw_combine_rule[0], raw_combine_rule[1])] = raw_combine_rule[2]
            
            opposed_rules = []
            (raw_opposed_rules, s) = extract_rules(s)
            for raw_opposed_rule in raw_opposed_rules:
                opposed_rules.append(get_sorted_seq(raw_opposed_rule[0], raw_opposed_rule[1]))
            opposed_rules = set(opposed_rules)
                
            (seq_length, seq_to_invoke) = s.split(" ", 1)
            
            elems_list = get_resulting_elems_list(seq_to_invoke, combine_rules, opposed_rules)
            
            output_f.write("Case #%d: [%s]\n" % (test_case_i + 1, ", ".join(elems_list)))
    
    finally:
        input_f.close()
        output_f.close()


main(sys.argv[1], sys.argv[2])
