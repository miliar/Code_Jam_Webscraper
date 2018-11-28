import sys

def getRow():
    r=int(raw_input())
    rows=[map(int,(raw_input()).split()) for i in range(0,4)]
    return rows[r-1]

T=int(raw_input())
for test in range(1,T+1):
    rows=[getRow(),getRow()]
    intersection=[a for a in rows[0] for b in rows[1] if a==b]
    if len(intersection)==0:
        print "Case #{0}: Volunteer cheated!".format(test)
    elif len(intersection)>=2:
        print "Case #{0}: Bad magician!".format(test)
    else:
        print "Case #{0}: {1}".format(test,intersection[0])
