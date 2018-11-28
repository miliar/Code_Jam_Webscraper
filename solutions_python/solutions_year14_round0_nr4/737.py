def getWarResult(girl_masses, boy_masses):
    girl_win = 0
    while len(girl_masses) > 0:
        girl = girl_masses.pop(0)
        arr = [x for x in boy_masses if x > girl]
        if len(arr) > 0:
            boy = min(arr)
        else:
            boy = min(boy_masses)
            girl_win = girl_win + 1
        boy_masses.remove(boy)
    return girl_win   
    
def getDeceitfulWarResult(girl_masses, boy_masses):
    #--- girl's strategy in brief ---
    #if girl lose inevitably, girl let boy push heaviest block
    #if girl can win by deceit, boy push lightest block
    #girl push blocks in order by weight (from light to heavy)
    girl_win = 0
    girl_masses.sort()
    while len(girl_masses) > 0:
        girl = girl_masses.pop(0)
        if girl < min(boy_masses):
            boy_masses.remove(max(boy_masses))
        else:
            boy_masses.remove(min(boy_masses))
            girl_win = girl_win + 1
    return girl_win  

test_cnt = input()
outputs = []
for num in range(0, test_cnt):
    block_cnt = input()
    girl_masses = [float(v) for v in raw_input().split(" ")]
    boy_masses = [float(v) for v in raw_input().split(" ")]
    normal_res = getWarResult(girl_masses[:], boy_masses[:])
    deceit_res = getDeceitfulWarResult(girl_masses[:], boy_masses[:])
    outputs.append([deceit_res, normal_res])
    
for i,v in enumerate(outputs):
    print "Case #%d: %d %d" % ((i + 1), v[0], v[1])

