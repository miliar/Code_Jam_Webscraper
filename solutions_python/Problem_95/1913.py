#!/usr/bin/env python
  
from string import lowercase
  
f=open('small.in')
o=open('small.out','w')
  
goog_talk=[x for x in 'ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyqez ']
  
real_talk=[x for x in 'ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupazoq ']
goog_to_real_map=dict(zip(goog_talk,real_talk))
real_to_goog_map=dict(zip(real_talk,goog_talk))
  
  
def goog_to_real(s):
    if s in goog_talk:
        return goog_to_real_map[s]
    else:
        return s
    #''.join([goog_to_real_map[ c ] for c in s])

def real_to_goog(s):
    if s in real_talk:
        return real_to_goog_map[s]
    else:
        return s
    #return ''.join([real_to_goog_map[ c ] for c in s])

num_cases=int(f.readline())
sentences=[f.readline()[:-1] for x in xrange(num_cases)]
for i,s in enumerate(sentences):
    o.write('Case #%d: %s\n'%(i+1,''.join([goog_to_real(c) for c in s])))

