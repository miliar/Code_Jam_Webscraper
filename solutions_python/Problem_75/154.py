def invoke(combine, opposed, z):
    #print combine, opposed, z
    x = ""
    for c in z:
        x += c
        #print x
        if x[-2:] in combine:
            x = x[:-2] + combine[x[-2:]]
        elif any(s[0] in x and s[1] in x for s in opposed):
            x = ""
    return x
    
def ar(s):
    return "[" + ", ".join(list(s)) + "]"
    
def test():
    print ar(invoke({'QF':'T','FQ':'T'}, ['QF'], 'FAQFDFQ'))

def main():
    cases = int(raw_input())
    for case in range(cases):
         data = raw_input().split(" ")
         c, data = int(data[0]), data[1:]
         combine, data = data[:c], data[c:]
         d, data = int(data[0]), data[1:]
         opposed, data = data[:d], data[d:]
         n, z = data[0], data[1]
         combine = dict([(s[:2],s[2]) for s in combine] + [(s[1::-1],s[2]) for s in combine])
         print "Case #%d: %s" % (case+1, ar(invoke(combine, opposed, z)))

main()
