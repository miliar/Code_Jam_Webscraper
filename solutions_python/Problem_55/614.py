#!/usr/bin/env python3
# import logging
# logging.basicConfig(filename='log',level=logging.DEBUG);
# lastLogger=logging.getLogger('sumLess_until');
# increasedLogger=logging.getLogger('increased');
# changedLogger=logging.getLogger('changed');
# caseLogger=logging.getLogger('Case');
T=int(input());

def sumLess_until(l,limit):
  for last in range(len(l)+2):
    if sum(l[:last])>limit:
      break;
  return last-1;

for Case in range(1,T+1):
  R,k,N=map(int,input().split());
  groups=list(map(int,input().split()));
  # caseLogger.debug('--------------------{}------------------------'.format(Case));
  ans=0;
  for turns in range(R):
    last=sumLess_until(groups,k);
    # lastLogger.debug('last={},which means choosed {}'.format(last,groups[:last]));
    # increasedLogger.debug('increased {}'.format(sum(groups[:last])));
    ans=ans+sum(groups[:last]);
    groups=groups[last:]+groups[:last];
    # changedLogger.debug('changed to {}'.format(groups));
  print('Case #{Case}: {ans}'.format(**locals()));

    
    
