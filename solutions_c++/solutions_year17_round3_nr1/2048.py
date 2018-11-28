#include <bits/stdc++.h>
#define rep(i,a,b) for(int i=(int)a;i<=(int)b;++i)
using namespace std;
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define SZ(x) (int)x.size()
#define ALL(x) x.begin(),x.end()
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vpii;
typedef long long ll;
const int N = 1e5+10,mod = 1e9+7;
int r[N],h[N];
const ll inf = 1e16;
ll dp[100][100][100];
void _main()
{
	int n,k;
	scanf("%d %d",&n,&k);
	vpii v;
	rep(i,1,n)
	{
		scanf("%d %d",r+i,h+i);
		v.pb(mp(r[i],h[i]));
	}
	sort(ALL(v));
	reverse(ALL(v));
	rep(i,1,n)
	{
		r[i] = v[i-1].x;
		h[i] = v[i-1].y;
	}
	memset(dp,-1,sizeof dp);
	rep(i,1,n) dp[i][1][i] = 2*1ll*r[i]*1ll*h[i];
	rep(i,2,n)
	{
		rep(j,1,i-1) rep(k,1,i-1) if(~dp[i-1][j][k])
		{
			dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k]);
			dp[i][j+1][i] = max(dp[i][j+1][i],dp[i-1][j][k] + (r[k]*1ll*r[k])-(r[i]*1ll*r[i]) + 2*1ll*r[i]*1ll*h[i]);
		}
	}
	ll res = -inf;
	rep(j,1,n) res = max(res,dp[n][k][j] + r[j]*1ll*r[j]);
	printf("%.16f\n", res*1.0*acos(-1));
}
int main(int argc, char const *argv[])
{
	int t;
	scanf("%d",&t);
	rep(i,1,t)
	{
		printf("Case #%d: ", i);
		_main();
	}
	return 0;
}