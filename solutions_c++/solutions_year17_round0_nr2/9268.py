#include<stdio.h>
#include<string.h>

int processVal(int tc, long int N )
{
  long int i, max=0, n = 0, nm=0;
  int found = 1;
  for (i=N; i> 0; i--){
    int val = i;
    found = 1; 
    //printf("Processing----------%d\n", i);
    do {
       max = val%10;
       n = val/10;
       val = n;
       nm = val%10;
       //printf("#%d %d %d\n", max, val, nm);
 
       if (nm <= max)
          continue;
       else 
          found=0; 
          break;
    } while(val>0);
    if(found)
      break;
  }
  
  printf("Case #%d: %ld\n", tc, i);
  return i;
}

int main(int argc, char *argv[])
{
   int T=0;
   long int k=0;
   scanf("%d",&T);
   for (int testcase = 1; testcase <= T; testcase++) {
     scanf("%d", &k);
     processVal(testcase , k);
   }
}

