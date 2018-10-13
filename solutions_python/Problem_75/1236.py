import sys
BASE_ELEMENTS = set('QWERTASDF')
if __name__ == "__main__":
    in_file = open(sys.argv[1])
    cases = eval(in_file.readline().strip())
    for case_num in xrange(cases):
        case_data = in_file.readline().strip().split(" ")
        non_base = dict()
        i = 1
        C = eval(case_data[0])
        for _ in xrange(C):
            non_base_combo = case_data[i]
            non_base[non_base_combo[0] + non_base_combo[1]] = non_base_combo[2]
            non_base[non_base_combo[1] + non_base_combo[0]] = non_base_combo[2]
            i += 1

        D = eval(case_data[i])
        i += 1
        opposites = dict()
        for _ in xrange(D):
            opposites[case_data[i][0]] = case_data[i][1]
            opposites[case_data[i][1]] = case_data[i][0]
            i += 1

        N = eval(case_data[i])
        i += 1
        series = case_data[i]
        combo = [series[0]]
        elements = {series[0]:1}
        element = 1
        
        while element < N:
            #print combo, elements, series[element]
            if combo == []:
                combo.append(series[element])
                elements[series[element]] = elements.get(series[element], 0) + 1
            else:
                non_base_element = non_base.get(combo[-1] + series[element])
                if non_base_element != None:
                    elements[combo[-1]] -= 1 
                    combo[-1] = non_base_element
                elif elements.get(opposites.get(series[element]), 0) > 0:
                    combo = []
                    elements = dict()
                else:
                    combo.append(series[element])
                    elements[series[element]] = elements.get(series[element], 0) + 1
            element += 1
                    

        if len(combo) >= 1:
            combo_str = combo[0]
            if len(combo) > 1:
                for el in combo [1:]:
                    combo_str += ', ' + el
        else:
            combo_str = ''
        
        print "Case #{0}: [{1}]".format(case_num + 1, combo_str)
                
            
