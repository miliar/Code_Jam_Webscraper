/*===============================================================
*  Filename£ºa.cpp
*  Author£ºzhuyutian
*  Date£º2017Äê04ÔÂ30ÈÕ
================================================================*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const int maxn = 1005;
const double PI = acos(-1);

int T,n,k;
int vis[maxn][maxn];
double dp[maxn][maxn];
struct Pa
{
	int r,h;
	bool operator<(const Pa& rhs) const
	{ return r == rhs.r ? h > rhs.h : r > rhs.r;}
}p[maxn];

double cs(ll x) { return  PI * x * x;}

double cal(int x,int h) { return PI * x * x * 2 + PI * 2 * x * h;}

double solve(int id,int c)
{
	if(c >= k) return  cal(p[id].r,p[id].h);
	if(vis[id][c]) return dp[id][c];
	vis[id][c] = 1;
	double& ans = dp[id][c];
	double s = cal(p[id].r,p[id].h);
	for(int i = id + 1; i < n; i++)
		ans = max(ans,solve(i,c + 1) + s - 2 * min(cs(p[id].r), cs(p[i].r)));
	return ans;
}

int main()
{
    freopen("a0.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>T;
	for(int kase = 1; kase <= T; kase++)
	{
		cin>>n>>k;
		double ans = 0;
		for(int i = 0; i < n; i++)
			cin>>p[i].r>>p[i].h;
		sort(p,p + n);
		memset(vis,0,sizeof(vis));
		memset(dp,0,sizeof(dp));
		for(int i = 0; i <= n - k; i++) 
		{
			double tmp = solve(i,1) - cs(p[i].r);
			ans = max(ans,tmp);
		}
		printf("Case #%d: %.9f\n",kase,ans);
	}
	return 0;
}
