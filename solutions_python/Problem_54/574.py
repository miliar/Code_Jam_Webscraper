import sys
import fractions

def fair_warning_case(input_file, output_file):
    great_data = map(int, input_file.readline().split())
    event_count = great_data[0]
    events = great_data[1:]
    optimum_anniversary = 0
    for i in range(event_count - 1):
        delta = abs(events[i + 1] - events[i])
        if optimum_anniversary == 0:
            optimum_anniversary = delta
        else:
            optimum_anniversary = fractions.gcd(optimum_anniversary, delta)
    apoc = -events[0] % optimum_anniversary
    output_file.write('%d\n' % apoc)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(1)
    
    input_file  = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')
    
    case_count = int(input_file.readline())
    for case in range(1, case_count + 1):
        output_file.write('Case #%d: ' % case)
        fair_warning_case(input_file, output_file)
    
    input_file.close()
    output_file.close()