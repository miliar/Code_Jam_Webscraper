SIZE    = 'large' # 'small'
INPUT   = 'b-' + SIZE + '.in'
OUTPUT  = 'b-' + SIZE + '.out'

DATASET = []
RESULT  = []

def read_input():
    with open(INPUT) as infile:
        infile.readline() # skip number of test cases
        for line in infile:
            C, F, X = line.strip().split()
            DATASET.append( (float(C), float(F), float(X)) )

def write_result():
    C = 0
    with open(OUTPUT, 'w') as outfile:
        for r in RESULT:
            C = C + 1
            rline = 'Case #%d: %.7f' % (C, r)
            
            print rline
            outfile.write(rline)
            outfile.write('\n')

def solve():
    for farm_price, farm_rate, target_cookies in DATASET:
        cookie_rate  = 2.0
        
        required_time = 0.0
        
        while True:
            time_without_farm  = target_cookies / cookie_rate
            time_with_new_farm = (farm_price / cookie_rate) + (target_cookies / (cookie_rate + farm_rate))
            
            if time_without_farm < time_with_new_farm:
                required_time += time_without_farm
                break
            else:
                required_time += (farm_price / cookie_rate)
                cookie_rate += farm_rate
        
        RESULT.append( required_time )

if __name__ == '__main__':
    read_input()
    solve()
    write_result()
    