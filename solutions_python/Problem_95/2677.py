import sys    
if __name__=="__main__":
   sys.setrecursionlimit(10000)
   input="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
   output="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"
   i=0   
   googlerasedict={}
   for x in input:
     if not x in list(googlerasedict):
       googlerasedict[x]=output[i]
     i=i+1
   googlerasedict['q']='z'
   googlerasedict['z']='q'
   lines = sys.stdin.readlines()
   for case_no,line in enumerate(lines[1:],start=1):
     
     tmp=""
     for y in line[0:len(line)-1]:
       if y != ' ' :
         tmp=tmp+y.replace(y,googlerasedict[y])
       elif y ==' ':
         tmp=tmp+y
         
     print "Case #%i:" %case_no+tmp   
   