import sys

CNT = 0
ITER = 1

mul = {
    '1':{'1':'1', 'i':'i', 'j':'j', 'k':'k'},
    'i':{'1':'i', 'i':'-1', 'j':'k', 'k':'-j'},
    'j':{'1':'j', 'i':'-k', 'j':'-1', 'k':'i'},
    'k':{'1':'k', 'i':'j', 'j':'-i', 'k':'-1'}
}
ANSWER = 'ijk'

def main():
    lengths = [int(n) for n in raw_input().split(' ')]
    nums = [n for n in raw_input()*lengths[ITER]]
    
    focus = 0

    negative = False

    for n in xrange(len(nums)-1):
        if ANSWER[focus] == nums[n]:
            #print "chk", nums[n] , n 
            focus += 1
            if focus == len(ANSWER):
                focus -= 1
            else:
                continue
        calc = mul[nums[n]][nums[n+1]]
        if '-' in calc:
            negative = ~negative
            calc = calc[1:]

        nums[n+1] = calc



    return 'YES' if not negative and focus == len(ANSWER)-1 and nums[-1] == ANSWER[-1] else 'NO'

if __name__=="__main__":
    #sys.stdin = open("D-small-attempt1.in", "r")
    #sys.stdout = open("D-output.txt", "w")

    for n in xrange(input()):
        
        print "Case #%d: %s" % (n+1, main())
