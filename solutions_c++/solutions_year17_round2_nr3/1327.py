#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#define fi first
#define se second
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,a,b) for (int i=(b);i>=(a);i--)
using namespace std;
typedef long long LL;

const int INF = 0x3f3f3f3f;

const int MAXN = 200; // 1e6;
int n,Q;
int T;
double G[MAXN][MAXN];
double e[MAXN],s[MAXN];
int u[MAXN],v[MAXN];

void doit(int i)
{
	int s = u[i],t=v[i];
}
double dp[MAXN];
void doitsmall()
{
	rep(i,1,n+1) dp[i]=1e18;
	dp[1]=0;
	rep(i,1,n)
	{
		double tmp = e[i], speed = s[i];
		double now = dp[i];
		rep(j,i+1,n+1)
		{
			tmp -= G[j-1][j];
			if (tmp <0) break;
			now += G[j-1][j]/s[i];
			dp[j] = min(dp[j],now);
		}
	}
	printf("%.8f", dp[n]);
}
int main()
{
	// freopen("in.txt","r",stdin);
	freopen("C-small-attempt1.in.txt","r",stdin);
	freopen("small.out","w",stdout);
	cin>>T;
	// cout<<(1e18>INF)<<endl;
	rep(cas,1,T+1)
	{
		cin>>n>>Q;
		rep(i,1,n+1) cin>>e[i]>>s[i];
		rep(i,1,n+1)
		{
			rep(j,1,n+1) cin>>G[i][j];
		}
		rep(i,1,Q+1) cin>>u[i]>>v[i];

		printf("Case #%d: ",cas );
		rep(i,1,Q+1)
		{
			doitsmall();
		}
		printf("\n");
	}
	


}

