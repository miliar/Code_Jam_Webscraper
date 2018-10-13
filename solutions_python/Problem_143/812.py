'''
Created on 3 May, 2014

@author: Ye Tian
'''
input = """5
2
mmaw
maw
2
gcj
cj
3
aaabbb
ab
aabb
2
abc
abc
3
aabc
abbc
abcc
"""

inputlist = input.split("\n");

task_number = 1#int(inputlist[0]);

initl = 1;
for i in range(0, task_number):
    tasks = int(inputlist[initl]);
    
    strings = [];
    sets = [];
    
    for j in range(0, tasks):
        strings.append(inputlist[initl+j+1]);
        sets.append(set(inputlist[initl+j+1]));
    
    print sets;
    
    
    
    