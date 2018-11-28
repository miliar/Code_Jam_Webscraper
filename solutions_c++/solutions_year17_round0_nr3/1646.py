#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int t;
long long n,k;
long long cnt[300][5];
long long val[300][5];
long long bi;
long long remains;
int mydiv;
void pri(long long a)
{
 long long a1,a2;
 a1=(long long)(a/2);
 a2=(a-1);
 a2=(long long)a2/2;
 printf("%I64d %I64d\n",a1,a2);
}
void clears(int a)
{
 val[a][1]=0;
 val[a][2]=0;
 cnt[a][1]=0;
 cnt[a][2]=0;
}
void solve()
{
 bi=2;
 mydiv=1;
 val[1][1]=n;
 cnt[1][1]=1;
 while(bi-1<k)
 {
  //printf("chk %I64d, %I64d\n",bi-1,k);
 // printf("%d : %I64d(%I64d) %I64d(%I64d)\n",mydiv,val[mydiv][1],cnt[mydiv][1],val[mydiv][2],cnt[mydiv][2]);
  bi=(long long)bi*2;
  mydiv++;
  clears(mydiv);
  val[mydiv][1]=val[mydiv-1][1]/2;
  cnt[mydiv][1]=cnt[mydiv-1][1];
  if((val[mydiv-1][1]-1)/2==val[mydiv][1]){cnt[mydiv][1]=cnt[mydiv][1]+cnt[mydiv-1][1];}
  else{val[mydiv][2]=(val[mydiv-1][1]-1)/2;cnt[mydiv][2]=cnt[mydiv][2]+cnt[mydiv-1][1];}
  if(val[mydiv-1][2]!=0)
  {
  if((val[mydiv-1][2])/2==val[mydiv][1]){cnt[mydiv][1]=cnt[mydiv][1]+cnt[mydiv-1][2];}
  else{val[mydiv][2]=(val[mydiv-1][2])/2;cnt[mydiv][2]=cnt[mydiv][2]+cnt[mydiv-1][2];}
  if((val[mydiv-1][2]-1)/2==val[mydiv][1]){cnt[mydiv][1]=cnt[mydiv][1]+cnt[mydiv-1][2];}
  else{val[mydiv][2]=(val[mydiv-1][2]-1)/2;cnt[mydiv][2]=cnt[mydiv][2]+cnt[mydiv-1][2];}
  }
 }
 bi=(long long)bi/2;
 bi=bi-1;
 remains=k-bi;
 //printf("remains %I64d\n",remains);
 //printf("%d : %I64d(%I64d) %I64d(%I64d)\n",mydiv,val[mydiv][1],cnt[mydiv][1],val[mydiv][2],cnt[mydiv][2]);
 if(cnt[mydiv][1]>=remains){pri(val[mydiv][1]);}
 else{pri(val[mydiv][2]);}
}
main()
{
 freopen("C-large.in","r",stdin);
 freopen("C-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%I64d%I64d",&n,&k);
  printf("Case #%d: ",tests);
  solve();
 }
 return 0;
}
