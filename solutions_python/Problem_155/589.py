
INPUT = "qualification\A-large.in"
OUTPUT = "qualification\A-large.out"

def solve(data):
    stand = 0
    result = 0
    for i,level in enumerate(data):
        if (i == 0):
            stand+=int(level)
            continue
        if level == '0':
            continue
        if (i > stand) :
            result += (i - stand)
            stand = i
        stand += int(level)
    return result

if __name__=="__main__":
    f_in = open(INPUT)
    f_out = open(OUTPUT,"w")
    lines = f_in.readlines()
    output = []
    i=1
    for line in lines[1:]:
        data = line.strip().split(" ")[1]
        output += "Case #%d: %d\n" % (i,solve(data))
        i+=1
    f_out.writelines(output)
    f_out.close()
    f_in.close()
    print 'done.'
