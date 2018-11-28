#include<bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define ll long long int
#define inf 1450000090
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d%d",&x,&y)
#define sdl(x) scanf("%lld",&x)
#define nax 100010
#define mp make_pair
#define sz(x) (int)(x.size())
#define pi pair <int , int>
#define pii pair < int , pair <int ,int > >
#define MOD 1000000007
using namespace std;
int speed[150];
int lt[150];
int mat[105][105];
double dp[105][105];
int dsum[105];
int main(int argc, char const *argv[])
{
  freopen("input.txt","read",stdin);
  freopen("output.txt","write",stdout);
  int t;
  sd(t);
  for(int tt=1;tt<=t;tt++)
  {
  	 printf("Case #%d: ",tt);
  	 int n,q;
  	 sd2(n,q);
  	 int a,b;
  	 for(int i=1;i<=n;i++)
  	 	sd2(lt[i],speed[i]);
  	 memset(mat,0,sizeof mat);
  	 memset(dsum,0,sizeof dsum);
  	 for(int i=1;i<=n;i++)
  	 {
  	 	for(int j=1;j<=n;j++)
  	 	{
  	 		sd(mat[i][j]);
  	 		if(mat[i][j]!=-1)
  	 			dsum[i+1] = dsum[i]+mat[i][j];
  	 		dp[i][j] = inf*1ll*inf;
  	 	}
  	 }
  	 for(int i=1;i<=n;i++)
  	 	dp[i][0] = inf*1ll*inf;
  		dp[1][0] = 0;
  	 for(int i=1;i<=q;i++)
  	 	sd2(a,b);// lite
  	 for(int i=2;i<=n;i++)
  	 {
  	 	double fans = inf*1ll*inf;
  	 	for(int j=1;j<=i-2;j++)
  	 	{
  	 		if(dsum[i]-dsum[j]<=lt[j])// use this horse
  	 		{
  	 			dp[i][j] = dp[i-1][j]+((dsum[i]-dsum[i-1])*1.0)/speed[j];
  	 		}
  	 	}
  	 	for(int j=0;j<=i-2;j++)
  	 		fans = min(fans,dp[i-1][j]);
  	 	if(dsum[i]-dsum[i-1]<=lt[i-1])
  	 		dp[i][i-1] = fans+((dsum[i]-dsum[i-1])*1.0)/speed[i-1];
  	 }
  	 double ans = inf*1ll*inf;
  	 for(int i=0;i<=n-1;i++)
  	 	ans = min(ans,dp[n][i]);
  	 printf("%0.15lf\n",ans);
  }
  return 0;
}