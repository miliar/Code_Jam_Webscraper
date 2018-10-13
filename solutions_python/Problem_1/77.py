# n, s, engines, queries
# Usage:
# python search.py > out.txt
f = None

def DoCase(n):
    s = int(f.readline())
    engines = []
    for i in range(s):
        engine = f.readline()
        engines += [engine]

    q = int(f.readline())
    queries = []
    for i in range(q):
        query = f.readline()
        queries += [query]

    used_eng = list(engines)
    num_switches = 0
    for q in queries:
        if q in used_eng:
            used_eng.remove(q)
            if not used_eng:
                num_switches += 1
                used_eng = list(engines)
                used_eng.remove(q)


    print 'Case #%d: %d' % (n, num_switches)
        
def main():
    global f
    f = file('in.txt', 'r')
    line = f.readline()
    for i in range(int(line)):
        DoCase(i + 1)

if __name__ == '__main__':
    main()
    


