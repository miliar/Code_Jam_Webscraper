import math

cases = int(input())




refs = {}


def refgen(number):
    global refs
    try:
        return refs[str(number)]
    except KeyError:
        sub_ref = {}
        if number == 0:
            return sub_ref

        sub_ref[str(math.ceil(number/2.0)-1)+'_'+str(math.floor(number/2.0))]=1
        if number == 1:
            return sub_ref
        temp = refgen(math.ceil(number/2.0)-1)
        for key in temp:
            try:
                sub_ref[key] += temp[key]
            except KeyError:
                sub_ref[key] = temp[key]
        temp = refgen(math.floor(number/2.0))
        for key in temp:
            try:
                sub_ref[key] += temp[key]
            except KeyError:
                sub_ref[key] = temp[key]
        refs[str(number)] = sub_ref
        return sub_ref
    












def solve(seats,people):
    splits = refgen(seats)
    ordered_splits = []
    for key in splits:
        ordered_splits.append([int(key.split('_')[0]),int(key.split('_')[1]),int(splits[key])])
    ordered_splits.sort()
    ordered_splits=list(reversed(ordered_splits))
    index = 0
    while ordered_splits[index][2] < people:
        people -= ordered_splits[index][2]
        index += 1
    return str(max(ordered_splits[index][0:2])) + ' ' + str(min(ordered_splits[index][0:2]))
            








for i in range(0,cases):
    inflow = str(input()).split(' ')
    seats = int(inflow[0])
    people = int(inflow[1])
    print("Case #"+str(i+1)+": "+ solve(seats,people))


