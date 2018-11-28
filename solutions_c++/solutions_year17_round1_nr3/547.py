/*input
4
11 5 16 5 0 0
3 1 3 2 2 0
3 1 3 2 1 0
2 1 5 1 1 1
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define F(i,a,b) for(ll i = a; i <= b; i++)
#define RF(i,a,b) for(ll i = a; i >= b; i--)
#define pii pair<ll,ll>
#define PI 3.14159265358979323846264338327950288
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define P(x) printf("%d\n",x)
#define all(v) v.begin(),v.end()
bool vis[101][101][101][101][2];
ll dp[102][102][102][102][2];
ll f(ll hd,ll ad,ll hk,ll ak,ll b,ll d,ll turn,ll H,ll HH)
{
	//cout<<"hd="<<hd<<"ad="<<ad<<"hk="<<hk<<"ak="<<ak<<endl;
	if(hd <= 0)
		return INF;
	if(hk <= 0)
		return 0;
	if(turn==0 && ad >= hk)
		return 1;
	if(turn == 1 && ak >= hd)
		return INF;
	if(vis[hd][ad][hk][ak][turn])
		return INF;
	if(dp[hd][ad][hk][ak][turn]!=-1)
		return dp[hd][ad][hk][ak][turn];
	vis[hd][ad][hk][ak][turn] = 1;
	if(turn==0) // players turn
	{
		ll ret1 = f(hd,ad,hk-ad,ak,b,d,turn^1,H,HH); // attack on knight
		ll ret2 = f(hd,ad+b,hk,ak,b,d,turn^1,H,HH); // increase attack
		ll ret3 = f(hd,ad,hk,max(0ll,ak-d),b,d,turn^1,H,HH); // decrease attack
		ll ret4 = f(H,ad,hk,ak,b,d,turn^1,H,HH); // cure
		vis[hd][ad][hk][ak][turn] = 0;
		return (dp[hd][ad][hk][ak][turn] = (min(ret1,min(ret2,min(ret3,ret4))) + 1));
	}
	else
	{
		ll ret = f(hd-ak,ad,hk,ak,b,d,turn^1,H,HH); // knight's move
		vis[hd][ad][hk][ak][turn] = 0;
		return (dp[hd][ad][hk][ak][turn] = (ret));
	}
}
int main() 
{
	std::ios::sync_with_stdio(false);
	freopen("is1.txt","r",stdin);
	freopen("os1.txt","w",stdout);
	ll tc=1;
	ll t;
	cin>>t;
	//S(t);
	while(t--)
	{
		memset(vis,0,sizeof(vis));
		memset(dp,-1,sizeof(dp));
		cout<<"Case #"<<tc++<<": ";
		ll hd,ad,hk,ak,b,d;
		cin>>hd>>ad>>hk>>ak>>b>>d;
		ll ans = f(hd,ad,hk,ak,b,d,0,hd,hk);
		if(ans >= INF)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		cout<<ans<<endl;
	}
	return 0;
}