#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

struct color{
 int col;
 int cnt;
 bool operator < (const color & o) const{
 return cnt>o.cnt;
 }
}A[7];
int t,n;
int lasts;
void pri(int a)
{
 if(a==1){printf("R");}
 if(a==2){printf("O");}
 if(a==3){printf("Y");}
 if(a==4){printf("G");}
 if(a==5){printf("B");}
 if(a==6){printf("V");}
}
//ROYGBV
main()
{
 freopen("B-small-attempt0.in","r",stdin);
 freopen("B-small-attempt0.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d",&n);
  for(int i=1;i<=6;i++)
  {
   A[i].col=i;
   scanf("%d",&A[i].cnt);
  }
  sort(&A[1],&A[7]);
  printf("Case #%d: ",tests);
  if(A[1].cnt>n/2){printf("IMPOSSIBLE\n");}
  else
  {
   while(A[1].cnt!=0)
   {
  // 	printf("in 1\n");
   	pri(A[1].col);A[1].cnt--;
   	if(A[2].cnt>A[3].cnt){pri(A[2].col);A[2].cnt--;lasts=2;}
   	else{pri(A[3].col);A[3].cnt--;lasts=3;}
   // printf("out 1\n");
   }
   while(A[2].cnt!=0||A[3].cnt!=0)
   {
   //	printf("in 2\n");
    if(lasts==2){pri(A[3].col);A[3].cnt--;lasts=3;}
    else{pri(A[2].col);A[2].cnt--;lasts=2;}
   }
   //printf("out 2\n");
   printf("\n");
  }
 }
 return 0;
}
