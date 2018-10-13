_in = open("A-small-attempt0.in", "r")
_out = open("A-small-attempt0.out", "wb");
err = ["Bad magician!","Volunteer cheated!"]
_num_test_cases = int(_in.readline().strip())
 
def pick_choose():
    v = _in.readline().strip()
    arr = []
    i = 0
    while i < 4:
        arr.append(_in.readline().strip())
        i += 1
    nums = arr[int(v) - 1].split(" ")
    return (v,nums)

def do_magic(r1, r2):
    f = 0
    n = None
    for i in r1:
        for j in r2:
            if i == j: 
                f += 1
                n = i
    return (f, n)
   
for t in range(0,_num_test_cases):
    i1, r1 = pick_choose()
    i2, r2 = pick_choose()
    rs,num = do_magic(r1,r2)
    if rs == 0:
        num = err[1]
    if rs > 1 :
        num = err[0]
    #print "case#%s: %s" %(t + 1, num)
    _out.write("Case #%s: %s\r\n" %(t + 1, num))
_out.close()
        
    
    