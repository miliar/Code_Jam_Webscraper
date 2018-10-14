
def run(elements_to_invoke, non_base_elements, opposite_elements):
    result = []
    for invoked in elements_to_invoke:
        if not result:
            result.append(invoked)
        else:
            r_combined = invoked + result[-1]
            combined = result[-1] + invoked

            non_base = non_base_elements.get(combined)
            if not non_base:
                non_base = non_base_elements.get(r_combined)
            if non_base:
                result[-1] = non_base
                continue
            # After you invoke an element, if it isn't immediately combined
            # to form another element, and it is opposed to something in your
            # element list, then your whole element list will be cleared.
            for opposite in opposite_elements:
                if invoked in opposite:
                    idx2 = (opposite.index(invoked) + 1) % 2
                    if opposite[idx2] in result:
                        #r_idx = -(result[::-1].index(opposite[idx2]) + 1)
                        result = []
                        break
            else:
                result.append(invoked)
    return result

if __name__ == "__main__":
    for i in xrange(int(raw_input())):
        line = raw_input().split(" ")
        c = int(line[0])
        non_base_elements = {}
        for j in xrange(c):
            non_base_elements[line[j + 1][:2]] = line[j + 1][2]
        d = int(line[c + 1])
        opposite_elements = line[c + 2:c + 2 + d]
        elements_to_invoke = line[c + 3 + d]

        result = run(elements_to_invoke, non_base_elements,
                     opposite_elements)
        print "Case #%d: [%s]" % (i + 1, ", ".join(result))
