#include<stdio.h>
#include<string.h>

int processVal(int tc, char *a, int k )
{
  int i,j;
  int count = 0;
  //printf("Proessing %s %d\n", a, strlen(a));

  for ( i = 0; i<=strlen(a)-k; i++){
   if(a[i]=='+') continue;
   count++;
   for(j = 0; j < k; j++){
      int t=i+j;
      if (a[t] == '-' )
         a[t] = '+'  ;    
      else 
         a[t] = '-' ;
    }
    //printf("%d %d %s \n", i, j, a);
  }
  if (strstr(a, "-"))
     printf("Case #%d: %s \n", tc, "IMPOSSIBLE");
  else 
     printf("Case #%d: %d \n", tc, count);
  return count;
}

int main(int argc, char *argv[])
{
   int T=0;
   int k=0;
   char pan[1000];
   scanf("%d",&T);
   for (int testcase = 1; testcase <= T; testcase++) {
     scanf("%s %d", pan, &k);
     processVal(testcase , pan, k);
   }
}

