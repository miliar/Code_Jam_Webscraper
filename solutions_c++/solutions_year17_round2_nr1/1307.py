#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int t;
double d;
int n;
int my;
double timeans;
double mypos;
double thiscut;
double mincut;
int posmincut;
double tmp1,tmp2;
struct node{
 double pos;
 double spd;
 bool operator < (const node &o) const{
 if(pos!=o.pos){return pos<o.pos;}
 else{return spd<o.spd;}
 }
}A[1005];
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  my=1;mypos=0;
  scanf("%lf%d",&d,&n);
  //printf("test %d\n",tests);
  //printf("pos %lf\n",d);
  for(int i=1;i<=n;i++)
  {
    scanf("%lf%lf",&A[i].pos,&A[i].spd);
    //printf("%lf %lf\n",A[i].pos,A[i].spd);
  }
  sort(&A[1],&A[n+1]);
  while(mypos<d)
  {
   posmincut=9999;
   mincut=2000000000;
   for(int i=my+1;i<=n;i++)
   {
   	if(A[i].spd<A[my].spd)
   	{
   	 tmp1=A[i].pos-A[my].pos;
   	 tmp2=A[my].spd-A[i].spd;
	 thiscut=tmp1/tmp2;
	 if(thiscut<mincut){mincut=thiscut;posmincut=i;}
	}
   }
   if(posmincut==9999){mypos=d;}
   else
   {
   mypos=A[posmincut].pos+(A[posmincut].spd*mincut);
  // printf("#cut %d at %.10lf\n",posmincut,mypos);
   if(mypos<d){my=posmincut;}
   }
  }
  tmp1=d-A[my].pos;
  tmp2=A[my].spd;
  timeans=tmp1/tmp2;
  //printf("my %d %lf\n",my,timeans);
  printf("Case #%d: %.10lf\n",tests,d/timeans);
 }
 return 0;
}
