import sys
VERBOSE = False
def resolve(overall_result_sheet, team_count):
    for team_index in range(team_count):
        result_sheet = overall_result_sheet[team_index]
        owp = 0
        for oponent in result_sheet['oponents']:
            op_result = overall_result_sheet[oponent]['oponents']
            wp_without = 0
            for t in op_result:
                if t != team_index:
                    wp_without += op_result[t]
            wp_without = float(wp_without) /( len(op_result) - 1 )
            owp += wp_without
        owp = float(owp) / len(result_sheet['oponents'])
        result_sheet['owp'] = owp
    for team_index in range(team_count):
        result_sheet = overall_result_sheet[team_index]
        oowp = 0
        for oponent in result_sheet['oponents']:
            oowp += overall_result_sheet[oponent]['owp']
        oowp = float(oowp) / len(result_sheet['oponents'])
        result_sheet['oowp'] = oowp
    if VERBOSE:
        print 'overall_result_sheet: ', overall_result_sheet
    for team_index in range(team_count):
        result_sheet = overall_result_sheet[team_index]
        print result_sheet['wp'] * 0.25 + \
              result_sheet['owp'] * 0.5 + \
              result_sheet['oowp'] * 0.25

            
    
def main():
    file = open(sys.argv[1])
    length = int(file.readline())
    for case_num in range(1, length+1):
        team_count = int(file.readline())
        overall_result_sheet = {}
        for team_index in xrange(team_count):
            results = file.readline()
            if VERBOSE:
                print 'results: ', results
            other_team = 0
            result_sheet = {'oponents':{}, 'wp':0}
            overall_result_sheet[team_index] = result_sheet
            win_count = 0
            for result in results:
                if result == '1':
                    result_sheet['oponents'][other_team] = 1
                    win_count += 1
                elif result == '0':
                    result_sheet['oponents'][other_team] = 0
                other_team += 1
            result_sheet['wp'] = float(win_count) / len(result_sheet['oponents'])
        print 'Case #%d:' %(case_num) 
        resolve(overall_result_sheet, team_count)
                    
if __name__ == '__main__':
    main()
