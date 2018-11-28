#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

#define INF 1000000000

int dp[110][110][110][4];
int cnt[10];

void su(int &a, int b)
{
	a=max(a,b);
}

void lemon()
{
	int n,P; scanf("%d%d",&n,&P);
	memset(cnt,0,sizeof cnt);
	rep(i,1,n) 
	{
		int x; scanf("%d",&x);
		cnt[x%P]++;
	}
	rep(i,0,100) rep(j,0,100) rep(k,0,100) rep(rm,0,2) dp[i][j][k][rm]=-INF;
	dp[0][0][0][0]=0;
	rep(i,0,100)
		rep(j,0,100)
			rep(k,0,100)
				rep(rm,0,3)
				{
					if (dp[i][j][k][rm]>=0)
					{
						int val=0;
						if (rm==0) val=1;
						val+=dp[i][j][k][rm];
						if (i<cnt[1]) su(dp[i+1][j][k][(rm+1)%P], val);
						if (j<cnt[2]) su(dp[i][j+1][k][(rm+2)%P], val);
						if (k<cnt[3]) su(dp[i][j][k+1][(rm+3)%P], val);
					}
				}
	
	int ans=0;
	rep(rm,0,3) su(ans,dp[cnt[1]][cnt[2]][cnt[3]][rm]+cnt[0]);
	printf("%d\n",ans);
			
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("A.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(i,1,tcase)
	{
		printf("Case #%d: ",i);
		lemon();
	}
	return 0;
}

