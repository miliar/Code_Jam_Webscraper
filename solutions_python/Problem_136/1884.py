def best_cookie(C, F, X):
    total_time = 0
    rate = 2 #cookies / sec
    while C/rate + X/(rate + F) < X/rate:
        total_time += C/rate
        rate += F
    total_time += X/rate
    return str(total_time)

def main():
    with open('outputLarge.txt','w') as o:
        with open('B-large.in', 'r') as f:
        #with open('sampleInput.txt', 'r') as f:
            T = int(f.readline())    
            for test_case in xrange(T):
                C, F, X = [float(x) for x in f.readline().split()]
                o.write("Case #" + str(test_case + 1) + ": " + best_cookie(C, F, X) + '\n')
    

if __name__ == '__main__':
    main()
