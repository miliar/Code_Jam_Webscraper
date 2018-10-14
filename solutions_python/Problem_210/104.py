# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 05:07:47 2017

@author: Tom
"""

fname = 'B-large.in'
oname = fname[:-3]+'.out'
with open(fname,'r') as f:
    with open(oname,'w') as o:
        T = int(f.readline().strip())
        for case in range(1,T+1):
            Ac,Aj = list(map(int,f.readline().strip().split()))
            print('Case {}: {},{}'.format(case,Ac,Aj))
            ACL = []
            for a in range(Ac):
                ACL.append(list(map(int,f.readline().strip().split())) + ['A'])
            AJL = []
            for a in range(Aj):
                AJL.append(list(map(int,f.readline().strip().split())) + ['J'])
            
            
            ACL = sorted(ACL,key=lambda p:p[0])
            AJL = sorted(AJL,key=lambda p:p[0])
            
            day = ['.']*1440
            for a in ACL+AJL:
                day[a[0]:a[1]] = [a[2]]*(a[1]-a[0])
            print(''.join(day))
            
            # Make a list of gaps
            gaps = []
            this = None
            left = day[0]
            for i,m in enumerate(day):
                if i==1439:
                    # last element
                    if this == None:
                        # not currently assembling a gap
                        if m == '.':
                            # A gap starts on the last character
                            if len(gaps) > 0:
                                if gaps[0][0] == 0:
                                    # the last gap wraps to the beginning
                                    gaps[0][0] = 1439
                                    gaps[0][2] = gaps[0][2] + 1
                                    gaps[0][3] = left
                                else:
                                    # make a new gap
                                    gaps.append([1439,0,1,left,day[0]])
                            else:
                                # make a new gap
                                gaps.append([1439,0,1,left,day[0]])
                        else:
                            # last character is not a gap
                            # that means a gap starting at zero might have this char as the left
                            if len(gaps) > 0:
                                if gaps[0][0] == 0:
                                    # first gap starts at 0, so its leftmost is this last character
                                    gaps[0][3] = m
                            
                    else:
                        # Currently assembling a gap, and we got to the end of the day
                        if m == '.':
                            # gap runs up to midnight, see if it combines with the first one
                            if len(gaps) > 0:
                                if gaps[0][0] == 0:
                                    # the last gap wraps to the beginning
                                    gaps[0][0] = this
                                    gaps[0][2] = gaps[0][2] + 1440-this
                                    gaps[0][3] = left
                                else:
                                    # make a new gap
                                    gaps.append([this,0,1440-this,left,day[0]])
                            else:
                                # make a new gap
                                gaps.append([this,0,1440-this,left,day[0]])
                        else:
                            # last gap ends one minute short of midnight
                            gaps.append([this,i,i-this,left,m])
                else:
                    # Middle element
                    if this == None:
                        # Not currently assembling a gap
                        if m == '.':
                            # start a gap
                            this = i
                        else:
                            # record a left char
                            left = m
                    else:
                        # Currently assembling a gap
                        if m == '.':
                            # continue the gap
                            pass
                        else:
                            # end of gap
                            gaps.append([this,i,i-this,left,m])
                            left = m
                            this = None
                
            gaps = sorted(gaps,key=lambda p:(p[2]))
            print(gaps)
            
            Aminutes = day.count('A')
            Jminutes = day.count('J')
            print(Aminutes,Jminutes)
            
            # Try to assign the gaps to each person
            filled = 0
            for g in [x for x in gaps if (x[3]=='A' and x[4]=='A')]:
                # gaps bordered on both sides
                if g[2] <= 720-Aminutes:
                    Aminutes = Aminutes + g[2]
                    if g[0] < g[1]:
                        for i in range(g[0],g[1]):
                            day[i] = g[3]
                    else:
                        for i in range(0,g[1]):
                            day[i] = g[3]
                        for i in range(g[0],1440):
                            day[i] = g[3]
                    print('Filled in gap ',g)
                    filled = filled+1
                    gaps.remove(g)
            
            for g in [x for x in gaps if (x[3]=='J' and x[4]=='J')]:
                # gaps bordered on both sides
                if g[2] <= 720-Jminutes:
                    Jminutes = Jminutes + g[2]
                    if g[0] < g[1]:
                        for i in range(g[0],g[1]):
                            day[i] = g[3]
                    else:
                        for i in range(0,g[1]):
                            day[i] = g[3]
                        for i in range(g[0],1440):
                            day[i] = g[3]
                    print('Filled in gap ',g)
                    filled = filled+1
                    gaps.remove(g)
            if filled > 0:
                print(''.join(day))
                print(gaps)
                print(Aminutes,Jminutes)
            
            instantHandoffs = 0
            for i in range(1440):
                if i == 1439:
                    if (day[i] == 'A' and day[0] == 'J') or (day[i] == 'J' and day[0] == 'A'):
                        instantHandoffs = instantHandoffs + 1
                        print('Instant handoff at midnight')
                else:
                    if (day[i] == 'A' and day[i+1] == 'J') or (day[i] == 'J' and day[i+1] == 'A'):
                        instantHandoffs = instantHandoffs + 1
                        print('Instant handoff')
            # Total number of handoffs
            totalHandoffs = instantHandoffs
            for g in gaps:
                if g[3] == g[4]:
                    totalHandoffs = totalHandoffs + 2
                    print('Double handoff')
                else:
                    totalHandoffs = totalHandoffs + 1
                    print('Single handoff')
            
            print('Total handoffs:',totalHandoffs)
            
            o.write('Case #{}: {}\n'.format(case,totalHandoffs))
            
            
            