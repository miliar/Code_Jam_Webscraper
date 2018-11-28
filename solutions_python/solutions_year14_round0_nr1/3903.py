'''
Created on 2014/04/12

@author: RYOKO
'''

T = int(raw_input())

inputs = []
for case in range(T) :
    ans1 = raw_input()
    cards1 = []
    for r in range(4):
        cards1.append(raw_input().split())
    ans2 = raw_input()
    cards2 = []
    for r in range(4):
        cards2.append(raw_input().split())
    inputs.append({'ans1':ans1, 'cards1': cards1, 'ans2': ans2, 'cards2': cards2})

count = 0
for input in inputs:
    count += 1
    cards1_set = set(input['cards1'][int(input['ans1'])-1])
    cards2_set = set(input['cards2'][int(input['ans2'])-1])
    hit_set = cards1_set & cards2_set
    hit = list(hit_set)
    hit_count = len(hit)
    if hit_count == 1:
        print "Case #" + str(count) + ": " + hit[0]
    if hit_count > 1:
        print "Case #" + str(count) + ": Bad magician!"
    if hit_count < 1:
        print "Case #" + str(count) + ": Volunteer cheated!"

    
    
