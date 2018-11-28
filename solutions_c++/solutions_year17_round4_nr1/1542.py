#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <cmath>
#define ld long double
using namespace std;
const int maxn = 100;
const int maxp = 4;
const ld cooling = 0.9999;
const ld t0 = 1e9;
const ld tim = 1.99;
int n,p,g[maxn+1],res,dem[maxp];
int dp[maxn+1][maxn+1][maxn+1][maxp];
int caldp(int x,int y,int z,int mod)
{
	if (dp[x][y][z][mod]==-1)
	{
		if (x==0 and y==0 and z==0) dp[x][y][z][mod]=0;
		else
		{
			dp[x][y][z][mod]=(mod==0);
			if (x>0) dp[x][y][z][mod]=max(dp[x][y][z][mod],caldp(x-1,y,z,(mod+1)%p)+(mod==0));
			if (y>0) dp[x][y][z][mod]=max(dp[x][y][z][mod],caldp(x,y-1,z,(mod+2)%p)+(mod==0));
			if (z>0) dp[x][y][z][mod]=max(dp[x][y][z][mod],caldp(x,y,z-1,(mod+3)%p)+(mod==0));
		}
	}
	return dp[x][y][z][mod];
}
void solve()
{
	cin >> n >> p;
	memset(dem,0,sizeof(dem));
	for (int i=1; i<=n; i++)
	{
		cin >> g[i];
		g[i]%=p;
		dem[g[i]]++;
	}
	memset(dp,-1,sizeof(dp));
	cout << dem[0]+caldp(dem[1],dem[2],dem[3],0);
}
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	srand(time(NULL));
	for (int i=1; i<=t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}