#import psyco
#psyco.full()

def getline():
    return f.readline().strip()

def getint():
    return int(f.readline().strip())

def log(msg):
#    print msg
    return

# from http://primes.utm.edu/lists/small/1000.txt
prime_data = """
      2      3      5      7     11     13     17     19     23     29 
     31     37     41     43     47     53     59     61     67     71 
     73     79     83     89     97    101    103    107    109    113 
    127    131    137    139    149    151    157    163    167    173 
    179    181    191    193    197    199    211    223    227    229 
    233    239    241    251    257    263    269    271    277    281 
    283    293    307    311    313    317    331    337    347    349 
    353    359    367    373    379    383    389    397    401    409 
    419    421    431    433    439    443    449    457    461    463 
    467    479    487    491    499    503    509    521    523    541 
    547    557    563    569    571    577    587    593    599    601 
    607    613    617    619    631    641    643    647    653    659 
    661    673    677    683    691    701    709    719    727    733 
    739    743    751    757    761    769    773    787    797    809 
    811    821    823    827    829    839    853    857    859    863 
    877    881    883    887    907    911    919    929    937    941 
    947    953    967    971    977    983    991    997
"""
prime_nums = [int(s.strip()) for s in prime_data.split()]

def is_int(num):
    return float(num) == float(int(num))

def find_prime_fac(x, P):
    fac = []
    for prime in prime_nums:
        if prime >= P and is_int(float(x) / prime):
            fac.append(prime)
        if prime > x:
            break
    log("p factors(%d, %d): %s" % (x, P, fac))
    return fac

def merge_sets(sets, x, y):
    log("merging: %s, %d, %d" % (sets, x, y))
    for i in sets.items():
        if i[1] == y:
            sets[i[0]] = x
    log("new set: %s" % sets)

def set_count(s):
    log("counting set %s" % s)
    seen = {}
    for i in s.items():
        if i[1] not in seen:
            seen[i[1]] = True
    return len(seen)

def do_case(case_num):
    """case_num is 1 based."""
    line = getline().split()
    A = int(line[0].strip())
    B = int(line[1].strip())
    P = int(line[2].strip())
    sets = {}
    for n in range(A, B + 1):
        sets[n] = n
    log(sets)
    for x in range(A, B):
        x_prime_facs = find_prime_fac(x, P)
        if len(x_prime_facs) == 0:
            continue
        for y in range(x + 1, B + 1):
            if sets[x] != sets[y]:
                y_prime_facs = find_prime_fac(y, P)
                if len(y_prime_facs) == 0:
                    continue
                for pf in x_prime_facs:
                    if pf in y_prime_facs:
                        merge_sets(sets, sets[x], sets[y])

    print "Case #%d: %d" % (case_num, set_count(sets))

def main():
    global f
    f = open('B-small-attempt1.in')
    cases = getint()
    for c in range(cases):
        do_case(c + 1)

if __name__ == '__main__':
    main()
#    print find_prime_fac(20, 6)
