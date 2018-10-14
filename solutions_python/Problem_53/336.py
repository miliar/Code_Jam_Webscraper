import sys

def snapper_chain_case(input_file, output_file):
    (devices, spans) = map(int, input_file.readline().split())
    if ((spans + 1) % pow(2, devices)) == 0:
        output_file.write('ON\n')
    else:
        output_file.write('OFF\n')  

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(1)
    
    input_file  = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')
    
    case_count = int(input_file.readline())
    for case in range(1, case_count + 1):
        output_file.write('Case #%d: ' % case)
        snapper_chain_case(input_file, output_file)
    
    input_file.close()
    output_file.close()