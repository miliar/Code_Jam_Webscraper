def is_light_on(snapper_count, snap_count):
    mask = 2 ** snapper_count - 1
    return (snap_count & mask) == mask
    
def main(input, output):
    case_count = int(input.readline())
    for i, line in enumerate(input):
        if i >= case_count: break
        
        light_state = is_light_on(*map(int, line.split()))
        print >> output, 'Case #%d: %s' % (i+1, 'ON' if light_state else 'OFF')
        
    
if __name__ == '__main__':
    import sys
    main(open(sys.argv[1]), sys.stdout)