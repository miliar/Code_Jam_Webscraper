#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# PLEASE PLEASE PLEASE don't judgme by this code.

def is_stink(pos_h, pos_w, m):
    val = m[pos_h][pos_w]
    try:
        if m[pos_h-1][pos_w] < val:
            return False
    except IndexError:
        pass
    try:
        if m[pos_h+1][pos_w] < val:
            return False
    except IndexError:
        pass
    try:
        if m[pos_h][pos_w-1] < val:
            return False
    except IndexError:
        pass
    try:
        if m[pos_h][pos_w+1] < val:
            return False
    except IndexError:
        pass
    return True

def drains_to(pos_h, pos_w, m, stinks):
    # North, West, East, South.
    val = m[pos_h][pos_w]

    # first check if it's a stink:
    if (pos_h, pos_w) in stinks:
        return (pos_h, pos_w)

    # then check the smalles values:
    try: 
        if pos_h-1>=0:
            north_value = (m[pos_h-1][pos_w], "N")
        else:
            north_value = (10, "N")
    except: 
        north_value = (10, "N")

    try:
        if pos_w-1>=0:
            west_value = (m[pos_h][pos_w-1], "W")
        else:
            west_value = (10, "W")
    except: 
        west_value = (10, "W")

    try:
        if pos_w+1<=len(m[0]):
            east_value = (m[pos_h][pos_w+1], "E")
        else:
            east_value = (10, "E")
    except:
        east_value = (10, "E")

    try: 
        if pos_h+1<=len(m):
            south_value = (m[pos_h+1][pos_w], "S")
        else:
            south_value = (10, "S")
    except: 
        south_value = (10, "S")

    l = list(set([i for i,p in (north_value, west_value, east_value, south_value)]))
    l.sort()
    min = l[0]
    l = [p for i,p in (north_value, west_value, east_value, south_value) if i == min]

    # finally check by position:
    if "N" in l and pos_h-1>=0 and m[pos_h-1][pos_w] < val:
        return drains_to(pos_h-1,pos_w,m,stinks)

    if "W" in l and pos_w-1>=0 and m[pos_h][pos_w-1] < val:
        return drains_to(pos_h,pos_w-1,m,stinks)

    if "E" in l and pos_w+1<=len(m[0]) and m[pos_h][pos_w+1] < val:
        return drains_to(pos_h,pos_w+1,m,stinks)

    if "S" in l and pos_h+1<=len(m) and m[pos_h+1][pos_w] < val:
        return drains_to(pos_h+1,pos_w,m,stinks)

data = []
for num, line in enumerate(file("B-small-attempt0.in")):
    data.append(line.strip())

map_count = int(data[0])

for i, line in enumerate(data):
    data[i] = map(int, line.split())

data = data[1:]

maps = []
map_complete = True
m = []
for line in data:
    if map_complete:
        map_complete = False
        H, W = line
        if len(m):
            maps.append(m)
            m = []
        continue
    else:
        m.append(line)

    if len(m) == H:
        map_complete = True

maps.append(m)


for id_map, m in enumerate(maps):
    stinks = []

    for pos_h, line_m in enumerate(m):
        for pos_w, line_n in enumerate(line_m):
            if is_stink(pos_h, pos_w, m):
                stinks.append((pos_h, pos_w))

    stinks_l = {}

    count = 0
    for pos_h, line_m in enumerate(m):
        for pos_w, line_n in enumerate(line_m):
            stink = drains_to(pos_h, pos_w, m, stinks)
            d = stinks_l.get(stink, {"fields": [], "letter": None})
            d["fields"].append((pos_h, pos_w))
            if not d["letter"]:
                d["letter"] = chr(97+count)
                count += 1
            stinks_l[stink] = d


    r = []
    for pos_h, line_m in enumerate(m):
        l = []
        for pos_w, line_n in enumerate(line_m):
            for stink in stinks_l.keys():
                if (pos_h, pos_w) in stinks_l[stink]["fields"]:
                    l.append(stinks_l[stink]["letter"])
        r.append(l)

    print "Case #%d:" % (id_map+1,)
    for l in r:
        print " ".join(l)
