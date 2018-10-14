import sys
# sys.stdin = open('in.txt','r')
# sys.stdout = open('out.txt', 'w')



def doCase(panList,currentCase):
    panList.sort(reverse=True)
    minmin = panList[0]

    for i in range(1,panList[0]+1):
        res = 0
        for pans in panList:
            if pans <= i:
                break
            res += (pans-1)/i
        if minmin > res + i:
            minmin = res + i

    print "Case #{}: {}".format(currentCase,minmin)



T = int(sys.stdin.readline())
for i in range(T):
    D = sys.stdin.readline()
    strList = sys.stdin.readline().split()
    panList = [int(n) for n in strList]
    doCase(panList,i+1)


# def doCase(panList,currentCase):
#     panList.sort(reverse=True)
#     state = {"minutes":0,"panList":panList}
#     def process(state):
#         pan = state["panList"]
#         if len(pan)==1:
#             if pan[0]<=3:     #eat them
#                 state["minutes"] += pan[0]
#                 state["panList"] = []
#             else:
#
#
#     def eat(state):
#         state["minutes"] += 1
#         state["panList"] = [i-1 for i in state["panList"] if i>1]
#
#     while state["panList"]:
#         process(state)
#     print "Case #{}: {}".format(currentCase,state["minutes"])