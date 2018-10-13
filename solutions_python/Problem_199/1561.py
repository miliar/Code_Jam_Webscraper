file = open("input")

counter_i = 1
counter_end_i = file.readline()
num = 1
statemem=set([])

def match(state):
    match_sign = 0
    length = len(state)-1
    pointer = 0
    while (match_sign==0 and pointer<=length):
        if state[pointer]=="-":
            match_sign=1
        else:
            pointer = pointer+1
    if match_sign ==1:
        return pointer
    if match_sign ==0:
        return length+1

def flip(state,position,num):
    length2=len(state)
    list1 = list(state)
    if (length2-position)<num:
        position = length2 - num
    c0=1
    while (c0<=num):
        if list1[position+c0-1]=="+":
            list1[position+c0-1]=str("-")
        else:
            list1[position+c0-1]=str("+")
        c0=c0+1
    state = ''.join(list1)
    return state

def remember(state):
    if state in statemem:
        return 0
    else:
        statemem.add(state)
        return 1

def solve(state, num):
    length=len(state)
    count = 0
    result = "0"
    pointer = match(state)
    while (pointer!=length):
        state = flip(state,pointer,num)
        if remember(state)==1:
            pointer = match(state)
            count=count+1
        else:
            result = "IMPOSSIBLE"
            return result
    result = str(count)
    return result
            


while (counter_i <= int(counter_end_i.strip())):
    current_line = file.readline().strip().split(' ')
    state=current_line[0]
    num = int(current_line[1])
    counter_i=counter_i+1
    statemem=set([])
    print "%s%d%s%s"%("Case #", counter_i-1, ": ",solve(state, num))
