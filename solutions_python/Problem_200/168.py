IN_FILE = "B_large.in"

infile = open(IN_FILE)
out = open("B.out","w")

cases = int(infile.readline())

def find_untidy(s):
    for i in range(1,len(s)):
        if int(s[i]) < int(s[i-1]):
            return i-1
    return -1

def clean(s,i):
    digit = len(s)-i-1
    s = s[:i+1]+("9"*(len(s)-i-1))
    n = int(s)
    s = str(n-10**digit)
    
    return s
    

for case in range(cases):
    print "\n"
    print "Case #%i" %(case+1)
    out.write("Case #%i: " %(case+1))
    
    s = infile.readline().strip()
    
    i = find_untidy(s)
    while i != -1:
        #print i
        s = clean(s,i)
        #print s
        i = find_untidy(s)
    
    print s
    out.write(s+"\n")
 
 
#fix line endings in input file   
infile.close()
infile = open(IN_FILE)
contents = infile.read()
infile.close()
infile = open(IN_FILE,"w")
infile.write(contents)
infile.close()
out.close()