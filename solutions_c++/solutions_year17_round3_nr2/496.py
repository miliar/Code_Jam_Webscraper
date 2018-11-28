#include <stdio.h>
#include <cstring>
#include <string>
using namespace std;
const int N=1440;

int dp[1450][1450][3];
int a[N+10];
void checkMin(int &aa, int b){ if(aa==-1 || aa > b)  aa=b;}
int main()
{
  //freopen("B-large.in","r",stdin);
  freopen("B-large.in","w",stdout);
  int test,cas(1);
  scanf("%d",&test);
  while(test--){
    int n,m;
    scanf("%d%d",&n,&m);
    memset(a,-1,sizeof(a));
    for(int i = 0; i < n+m; ++i){
      int s,e;
      scanf("%d%d",&s,&e);
      for(int j=s+1;j<=e;++j){
        a[j]=(i<n?1:2);
      }
    }
    memset(dp,-1,sizeof(dp));
    dp[0][0][0]=dp[0][0][1]=1;
    for(int i=1;i<=1440;++i){
      for(int j = 0; j<=i&&j<=720;++j){
        for(int k=0;k<2;++k){
          if(dp[i-1][j][k]==-1) continue;
          if(a[i]==1 || a[i]==-1){
            checkMin(dp[i][j][1],dp[i-1][j][k]+(k==0));
     //       if(i<10 && j<10) printf("dp1:%d %d %d\n",i,j,dp[i][j][1]);
          }
          if(a[i]==2 || a[i]==-1){
            checkMin(dp[i][j+1][0],dp[i-1][j][k]+(k==1));
     //       if(i<10 && j<10)printf("dp0:%d %d %d\n",i,j+1,dp[i][j+1][0]);
          }
    //      if(i==1440||j>=700) printf("%d %d %d %d\n",i,j,k,dp[i][j][k]);
        }
      }
    }
//    printf("%d %d\n",dp[1440][720][0],dp[1440][720][1]);
    int ans=dp[1440][720][0];
    if(dp[1440][720][1]!=-1) {
      checkMin(ans,dp[1440][720][1]);
    }
    if(ans > 2) ans --;
    printf("Case #%d: %d\n",cas++,ans);

  }

  return 0;
}
/* sw=2;ts=2;sts=2;expandtab */
