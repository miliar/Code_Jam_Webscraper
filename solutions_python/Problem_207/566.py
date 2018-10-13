
import random
import sys
sys.setrecursionlimit(10000000)
def can_coexist(unicorn1,unicorn2):
    if unicorn1 == "R":
        return unicorn2 == 'Y' or unicorn2 == "B" or unicorn2 == "G"
    if unicorn1 == "B":
        return unicorn2 == "R" or unicorn2 == "Y" or unicorn2 == "O"
    if unicorn1 == "Y":
        return unicorn2 in ["R",'B','V']
    if unicorn1 == "O":
        return unicorn2 in ["B"]
    if unicorn1 == "G":
        return unicorn2 == "R"
    if unicorn1 == "V":
        return unicorn2 == "Y"

assert can_coexist("R","B")
assert can_coexist("B","R")
assert not can_coexist("V","G")
assert not can_coexist("G","V")
assert not can_coexist("R","R")

def pairs(iteratable):
    p2 = None
    for p1 in iteratable:
        if p2:
            yield p2, p1
        p2 = p1
def is_stable(unicorn_string):
    for uni1, uni2 in pairs(unicorn_string):
        if not can_coexist(uni1,uni2):
            return False
    return can_coexist(unicorn_string[0],unicorn_string[-1])

assert is_stable("RYB")
assert not is_stable("RYBR")
assert not is_stable("RYOB")

R_INDEX = 0
O_INDEX = 1
Y_INDEX = 2
G_INDEX = 3
B_INDEX = 4
V_INDEX = 5

NAMES_UNICORNS = "ROYGBV"

def my_argmax(array):
    max = array[0]
    idxmax = 0
    for idx, num in enumerate(array):
        if num > max:
            max = num
            idxmax = idx
    return max, idxmax

def sort_unicorns(array):
    tosort = []
    for index,countremaining in enumerate(array):
        tosort.append((countremaining,index,NAMES_UNICORNS[index]))
    tosort.sort(reverse=True)
    return tosort

def is_impossible(remainingunicorncount):
    if remainingunicorncount[R_INDEX] + remainingunicorncount[O_INDEX] + remainingunicorncount[V_INDEX] > remainingunicorncount[B_INDEX] + remainingunicorncount[Y_INDEX] + remainingunicorncount[G_INDEX]:
        return True
    if remainingunicorncount[B_INDEX] + remainingunicorncount[G_INDEX] + remainingunicorncount[V_INDEX] > remainingunicorncount[R_INDEX] + remainingunicorncount[Y_INDEX] + remainingunicorncount[O_INDEX]:
        return True
    if remainingunicorncount[Y_INDEX] + remainingunicorncount[O_INDEX] + remainingunicorncount[G_INDEX] > remainingunicorncount[R_INDEX] + remainingunicorncount[B_INDEX] + remainingunicorncount[V_INDEX]:
        return True
    return False

def greedy_search_stable(start,remainingunicorncount,depthhere = 0):
    #print(remainingunicorncount)
    #print(str(depthhere) + " remaining: " + str(sum(remainingunicorncount)))
    sortedunicrons = sort_unicorns(remainingunicorncount)
    if len(start) == 0:
        for remaining, index, name in sortedunicrons:
            if remaining > 0:
                newstart = name
                nowremaining = [a for a in remainingunicorncount]
                nowremaining[index] = remaining-1
                result = greedy_search_stable(newstart,nowremaining,depthhere+1)
                if result:
                    return result
        else:
            return "IMPOSSIBLE"
    if sum(remainingunicorncount) == 0:
       # print("reached the end: " + start)
        if is_stable(start):
            return start
        else:
            return None

    # make new solution
    lastunicornpicked = start[-1]
    for remaining, index, name in sortedunicrons:
        if remaining > 0 and can_coexist(lastunicornpicked,name):
            #print("picking " + name)
            newstart = start + name
            nowremaining = [a for a in remainingunicorncount]

            nowremaining[index] = remaining - 1
            #print("With start " + start + " remaining: " + str(nowremaining))
            result = greedy_search_stable(newstart, nowremaining,depthhere+1)
            if result:
                return result


def stresstest(maxunicorns = 1000, testcases=100, allowStrangeUnicorns = False):
    for _ in range(testcases):
        if allowStrangeUnicorns:
            tofill = [random.randint(0,maxunicorns/2),random.randint(0,maxunicorns/2),random.randint(0,maxunicorns/2),random.randint(0,maxunicorns/2),random.randint(0,maxunicorns/2),random.randint(0,maxunicorns/2)]
        else:
            tofill = [random.randint(0, maxunicorns / 2), 0,
                      random.randint(0, maxunicorns / 2), 0,
                      random.randint(0, maxunicorns / 2), 0]
        if(is_impossible(tofill)):
            print("IMPOSSIBLE")
        else:
            print("Not impossible. let's start: " + str(tofill))
            result = greedy_search_stable("",tofill)
            print(result)
            if result != "IMPOSSIBLE":
                assert len(result) == sum(tofill)
    print("DONE!")

greedy_search_stable("",[50,0,26,0,26,0])

tests = [[1,0,2,0,0,0],[2,0,2,0,2,0],[2,0,1,1,2,0],[0,0,2,0,0,2]]
assert greedy_search_stable("",[1,0,2,0,0,0]) == "IMPOSSIBLE"
print(greedy_search_stable("",[2,0,2,0,2,0]))
print(greedy_search_stable("",[1,0,2,0,0,0]))
print(greedy_search_stable("",[2,0,1,1,2,0]))
print(greedy_search_stable("",[0,0,2,0,0,2]))

print("Testing impossible")
for t in tests:
    print(is_impossible(t))



#stresstest(maxunicorns=800,allowStrangeUnicorns=True)
with open("bsmall.in") as infile:
    with open('outputsmall.out','w') as outfile:
        t = int(infile.readline())
        for casenum in range(t):
            ponies = [int(a) for a in infile.readline().split()]
            ponies = ponies[1:]
            if is_impossible(ponies):
                outfile.write("Case #" + str(casenum+1) + ": IMPOSSIBLE\n")
            else:
                outfile.write("Case #" + str(casenum+1) + ": " + greedy_search_stable("",ponies) + "\n")


