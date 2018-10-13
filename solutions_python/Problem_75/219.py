#/usr/bin/env python

import sys


DEBUG = False
def debug(string):
    if DEBUG:
        print string


def init_case(items):
    combinations = []
    comb_num = int(items.next())
    for i in range(comb_num):
        item = items.next()
        combinations.append({
            "el1": item[0],
            "el2": item[1],
            "result": item[2]
        })
    debug("Combinations: %s -> %s" % (comb_num, combinations))
    opposed = []
    opposed_num = int(items.next())
    for i in range(opposed_num):
        item = items.next()
        opposed.append({
            "el1": item[0],
            "el2": item[1]
        })
    debug("Opposed: %s -> %s" % (opposed_num, opposed))
    elements_num = int(items.next())
    elements = items.next()
    debug("Elements: %s -> %s" % (elements_num, elements))
    return [combinations, opposed, elements]


def check_comb(info, combinations):
    el1 = info["element"]
    el2 = info["element_list"][-1]
    for combination in combinations:
        if el1 == combination["el1"] and el2 == combination["el2"]:
            info["element_list"] = info["element_list"][0:-1]
            info["element_list"].append(combination["result"])
            return True
        elif el1 == combination["el2"] and el2 == combination["el1"]:
            info["element_list"] = info["element_list"][0:-1]
            info["element_list"].append(combination["result"])
            return True
    info["element_list"].append(info["element"])
    return False


def check_opposed(info, opposed):
    element = info["element_list"][-1]
    element_list = info["element_list"][0:-1]
    for oppose in opposed:
        if element == oppose["el1"]:
            for key, value in enumerate(element_list):
                if value == oppose["el2"]:
                    info["element_list"] = []
                    return True
        elif element == oppose["el2"]:
            for key, value in enumerate(element_list):
                if value == oppose["el1"]:
                    info["element_list"] = []
                    return True
    return False


in_file = sys.argv[1]
fp = open(in_file)
for case in range (1, int(fp.readline())+1):
    # Init
    debug("Case %s: " % (case))
    info = {
        "element": False,
        "element_list": []
    }
    [combinations, opposed, elements] = init_case(iter(fp.readline().split()))
    # Body
    for element in elements:
        info["element"] = element
        if len(info["element_list"]) == 0:
            info["element_list"].append(element)
        else:
            check_comb(info, combinations)
            check_opposed(info, opposed)
    # Finish
    out = "["
    for element in info["element_list"]:
        out += element + ", "
    if len(out) > 1:
        out = out[0:-2]
    out += "]"
    print "Case #%s: %s" % (str(case), out)
    debug("")