#!/usr/bin/python

T = int(raw_input())
for i in xrange(T):
    smax, audience = raw_input().split()
    audience = list(audience)
    invitees = cuml_audience = 0
    for a in xrange(len(audience)):
        cuml_audience += int(audience[a])
        invitees = max(invitees, a+1-cuml_audience)
    print('Case #' + str(i+1) + ': ' + str(invitees))
        
