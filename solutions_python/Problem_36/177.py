
SUBSTRING = "welcome to code jam"
MODULUS = 10000

def count_instances(substring, mainstring):
    counters = [1 for i in xrange(len(mainstring))]
    
    for i, sch in enumerate(substring):
        next_counters = [0 for k in xrange(len(mainstring))]
        current_count = 0
        for j, mch in enumerate(mainstring):
            if sch==mch:
                current_count = (current_count + counters[j]) % MODULUS
            next_counters[j] = current_count
        counters = next_counters

    return counters[-1]
        
def main():
    cases = int(raw_input().strip())
    for i in xrange(cases):
        casestring = raw_input().strip()
        count = count_instances(SUBSTRING, casestring)
        print "Case #{0}: {1}".format(i+1, str(count).zfill(4))

if __name__=="__main__":
    main()
