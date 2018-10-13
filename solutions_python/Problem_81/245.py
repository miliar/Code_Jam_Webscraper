def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        num_of_opp = int(fh.readline().strip())
        idx = 0
        opp_map = dict()
        while (idx < num_of_opp):
            opp_map[idx] = list(fh.readline().strip())
            idx = idx + 1
                        
        test_data[count] = opp_map
        count = count + 1
    
    fh.close()
    return test_data

def _execute_test(test_data):
    print test_data
    
    opp_map = dict()
    for (k, v) in test_data.items():
        player_idx = k
        wins = 0
        lose = 0
        opponents = list()
        opp_idx = 0
        for o in v:
            if o == '1':
                wins += 1
                opponents.append(opp_idx)
            elif o == '0':
                lose += 1
                opponents.append(opp_idx)
                
            opp_idx += 1
            
        win_percent = float(wins)/(wins + lose)
        opp_map[player_idx] = (win_percent, opponents)
    
    print "WP: %s" % opp_map
    
    #  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
    owp_map = dict();
    for (k,v) in opp_map.items():
        owp = 0
        
        for opp in v[1]:
            opp_wins = 0
            opp_lose = 0
            opp_opp = opp_map[opp][1]
            for oo in opp_opp:
                if oo != k:
                    if test_data[opp][oo] == '1':
                        opp_wins += 1
                    elif test_data[opp][oo] == '0':
                        opp_lose += 1
                        
            owp += float(opp_wins) / (opp_wins + opp_lose)
            
        owp = float(owp) / len(v[1])
        owp_map[k] = owp
        
    print "OWP: %s" % owp_map
    
    oowp_map = dict()
    for (k,v) in opp_map.items():
        oowp = 0
        for opp in v[1]:
            oowp += owp_map[opp]
        
        oowp = float(oowp) / len(v[1])
        oowp_map[k] = oowp
        
    print "OOWP: %s" % oowp_map
    
    rpi_map = dict()
    for (k,v) in opp_map.items():
        rpi = (0.25 * v[0]) + (0.50 * owp_map[k]) + (0.25 * oowp_map[k])
        rpi_map[k] = "%.12f" % rpi
        
    print "RPI: %s" % rpi_map
        
    return rpi_map

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s:\n" % test_id)
        output.write("%s\n" % "\n".join(test_result.values()))
        
    output.close()
    
if __name__ == '__main__':
    main()