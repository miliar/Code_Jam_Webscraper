#encoding=utf8
filename = "A-large.in"
raw_data = ''
with open(filename, 'r') as f:
        raw_data = f.read().split('\n')

ans = [False] * 1000
test_count = int(raw_data.pop(0))
for test in range(test_count):
        question = raw_data.pop(0)
        cur = question.split(' ')
        pancake = cur.pop(0)
        pcount = len(pancake)
        filp = int(cur.pop(0))
        for c in range(pcount):
                if pancake[c] == '+':
                        ans[c] = True
                else:
                        ans[c] = False

        filpCount = 0
        end = pcount - filp + 1
        for c in range(end):
                if ans[c] == False:
                        for d in range(filp):
                                ans[d+c] = not ans[d+c]
                        filpCount=filpCount+1

        isPass = True
        for c in range(pcount):
                if ans[c] == False:
                        isPass = False

        if isPass == True:
                print "Case #%d:"%(test+1),filpCount
        else :
                print "Case #%d: IMPOSSIBLE"%(test+1)
