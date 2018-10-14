import sys
quaternion = {
        '1':{'1':('1',True),'i':('i',True),'j':('j',True),'k':('k',True)},
        'i':{'1':('i',True),'i':('1',False),'j':('k',True),'k':('j',False)},
        'j':{'1':('j',True),'i':('k',False),'j':('1',False),'k':('i',True)},
        'k':{'1':('k',True),'i':('j',True),'j':('i',False),'k':('1',False)},
        }

def processTest():
    nums = [int(x) for x in f.readline().split(' ')]
    l = nums[0]
    x = nums[1]
    line = f.readline()[:-1]
    #print('+++++++++++')
    #print(line+' x'+str(x))

    if len(line) != l:
        print('OMG EPIC FAIL on num length')
        
    ijks = {'i':0,'j':0,'k':0}
    for c in line:
        ijks[c]=1
    if ijks['i']+ijks['j']+ijks['k'] == 1:
        return 'NO'
    tokens = ''.join([line for i in range(x)])
    splits = [0,0,0]
    def advanceUntil(ijk,pos):
        start = splits[max(0,pos-1)]
        startQuat = '1' if pos>0 or start==0 else ijk
        splits[pos] = start
        #print('advancing: '+ijk + ' from: '+str(start))

        current = [startQuat,True]
        while splits[pos]<len(tokens):
            new = quaternion[current[0]][tokens[splits[pos]]]
            current[0] = new[0]
            current[1] = not current[1] ^ new[1]
            #print(current,tokens[splits[pos]])
            splits[pos]+=1
            if pos!=2 and current[0] == ijk and current[1]:
                break
        #print(ijk+': '+tokens[start:(splits[pos])]+' = ' + str(current))
        if current[0] == ijk and current[1]:
            return True
        return False

    if not advanceUntil('i',0) or not advanceUntil('j',1) or not advanceUntil('k',2):
        return 'NO'
    return 'YES'

f = open(sys.argv[1],'r')
maxtests = int(f.readline())
testnum = 1
while testnum <= maxtests:
    answer = processTest()
    print('Case #'+str(testnum)+': '+ answer)
    testnum +=1

f.close()
