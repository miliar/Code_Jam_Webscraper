import sys,  os

def invoke(line):
    li = line.split()
    combine_num = int(li.pop(0))
    combine = dict()
    oppose = []
    for k in range(combine_num):
        str = li.pop(0)
        combine[str[0:2]] = str[2:3]
    oppose_num = int(li.pop(0))
    for k in range(oppose_num):
        str = li.pop(0)
        oppose.append(str)
    ele_num = li.pop(0)
    ele = li.pop(0)
    str = ''
    for x in ele:
        str += x
        if len(str) == 1:
            continue
        elif((str[-2:] in combine)):
            if len(str) == 2:
                str = combine[str[-2:]]
            else:
                str = str[:-2] + combine[str[-2:]]
        elif str[-1]+str[-2] in combine:
            if len(str) == 2:
                str = combine[str[-1]+str[-2]]
            else:
                str = str[:-2] + combine[str[-1]+str[-2]]
        else:
            for x in str[:-1]:
                if str[-1:]+x in oppose:
                    str = ''
                elif x+str[-1:] in oppose:
                    str = ''
    return str

T = int(sys.stdin.readline())  
for i in range(T):
    out = invoke(sys.stdin.readline())
    if len(out) == 0:
        ans = '[]'
    else:
        ans ='['
        for x in out:
            ans += (x + ', ')
        ans = ans[:-2] + ']'
    print "Case #%d: " %( i+1) + ans
