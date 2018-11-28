import sys

def process_case():
    C, F, X = [float(x) for x in sys.stdin.readline().strip().split(' ')]
    base_rate = 2

    elapsed = 0
    current_rate = base_rate
    
    buy_time = C / current_rate + X / (current_rate + F)
    wait_time = X / current_rate

    while (buy_time < wait_time):
        elapsed += C / current_rate
        current_rate += F
        
        buy_time = C / current_rate + X / (current_rate + F)
        wait_time = X / current_rate

    elapsed += wait_time
    return '%.7f' % (elapsed,)
        

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        result = process_case()
        print 'Case #%d: %s' % (i + 1, result)

if __name__ == '__main__':
    main()
