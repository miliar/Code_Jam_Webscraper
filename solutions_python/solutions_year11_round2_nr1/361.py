import sys
import re

#helper
def get_wp(mat,j,d,excl=-1):
    sum = 0
    cnt = 0
    #print 'ln %s' % str(mat[j])
    for k in range(0,d):
        #print "j,k: %i, %i"  % (j,k)
        if excl==-1 or excl!=k:
            if mat[j][k] in ['0','1']:
                cnt+=1
                if mat[j][k] == '1':
                    sum+=1
    
    if cnt == 0:
        #print 'team: %i sum %i has count 0' % (j,sum)
        return 0
    else:
        #print 'team: %i sum %i cnt %i rslt %.2f' % (j,sum,cnt,float(sum)/cnt)
        return float(sum)/cnt
        
def get_owp(mat,team,dim):
    wpsum = 0.0
    cnt = 0
    for k in range(0,d):
        #print "j,k: %i, %i"  % (j,k)
        if mat[team][k] in ['0','1']:
            wp1 = get_wp(mat,k,d,team)
            #print 'team %i played against team %i, add wp %.2f' % (team,k,wp1)
            cnt+=1
            wpsum+=wp1

    if cnt == 0:
        return 0
    else:
        return wpsum/cnt
        
def get_oowp(mat,owp,team,dim):
    owpsum = 0.0
    cnt = 0
    for k in range(0,d):
        if mat[team][k] in ['0','1']:
            #wp1 = get_owp(mat,k,d)
            #print 'team %i played against team %i, add wp %.2f' % (team,k,wp1)
            cnt+=1
            owpsum+=owp[k]

    if cnt == 0:
        return 0
    else:
        return owpsum/cnt
#end helper

write = 'write' in sys.argv
filein = sys.argv[1]
fileout = re.sub('\.in','',filein) + ".out"
fin = open(filein,'r')
if write: fout = open(fileout,'w')
    
n = int(fin.readline())
print 'tot: %s' % n

for i in range(1,n+1):
    d = int(fin.readline()[0:-1])
    print 'dim: %i' % d
    mat = list()
    for j in range(1,d+1):
        ln = fin.readline()[0:-1];
        mat.append(list(ln))
        if not write: print ln
    
    
    WP = list()
    OWP = list()
    OOWP = list()
    RPI = list()
    for j in range(0,d):
        WP.append(get_wp(mat,j,d))
        
    for j in range(0,d):
        OWP.append(get_owp(mat,j,d))
        
    for j in range(0,d):
        OOWP.append(get_oowp(mat,OWP,j,d))
        
    for j in range(0,d):
        RPI.append(0.25*WP[j]+0.5*OWP[j] + 0.25 * OOWP[j])
    
    sol = "Case #%i:\n" % i
    for j in range(0,d):
        sol+= '%.12f\n' % RPI[j]
    if not write: print sol
    if not write: print '==================='
    if write: fout.write(sol)

if write: fout.close()