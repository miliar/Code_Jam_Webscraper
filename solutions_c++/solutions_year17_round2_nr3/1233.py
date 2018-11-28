#include <stdio.h>
#include <stdlib.h>

struct city{
double spd;
double pow;
}A[1001];
int t;
int n;
int q;
int st,ed;
double ans;
double dis[1001][1001];
double dp[1001][1001];
void clr()
{
 for(int i=1;i<=1000;i++)
 {
  for(int j=i;j>=0;j--)
  {
   dp[i][j]=100000000008;
  }
 }
 dp[1][0]=0;
}
void solvesmall()
{
double tmp;
double times;
int at;
 for(int i=1;i<n;i++)
 {
  for(int j=0;j<i;j++)
  {
   if(dp[i][j]!=(-1))
   {
   	tmp=A[i].pow;
   	at=i;
   	while(at<n)
   	{
	 if(tmp-dis[at][at+1]>=0)
	 {
	  tmp=tmp-dis[at][at+1];
	  times=A[i].pow-tmp;
	  times=times/A[i].spd;
	  if(times+dp[i][j]<dp[at+1][i]){dp[at+1][i]=times+dp[i][j];}
	  at++;
	 }
	 else{at=n;}
	}
   }
  }
 }
 ans=100000000005;
 for(int i=n-1;i>=1;i--)
 {
  //printf("dp %d : %.10lf\n",i,dp[n][i]);
  if(ans>dp[n][i]){ans=dp[n][i];}
 }
 printf("%.10lf\n",ans);
}
main()
{
 freopen("C-small-attempt1.in","r",stdin);
 freopen("C-small-attempt1.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d%d",&n,&q);
  for(int i=1;i<=n;i++)
  {
   scanf("%lf%lf",&A[i].pow,&A[i].spd);
  }
  for(int i=1;i<=n;i++)
  {
  	for(int j=1;j<=n;j++)
  	{
  		   scanf("%lf",&dis[i][j]);
  		  // printf("%lf ",dis[i][j]);
	  }
//printf("\n");
  }
  for(int i=1;i<=q;i++)
  {
   scanf("%d%d",&st,&ed);
  }
  printf("Case #%d: ",tests);
  clr();
  solvesmall();
 }
 return 0;
}
