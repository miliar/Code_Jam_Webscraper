#include<bits/stdc++.h>
using namespace std;
#define fs first
#define sc second
#define MAX 100000
#define pb push_back
#define mp make_pair
#define INF (1LL<<61)
#define MOD 1000000007
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
vii V;
double pi=3.141592653589;
Int dp[1100][1100],N,K;
Int solve(Int i,Int j)
{
	if (j==0)
		return 0;
	if (j>i)
		return 0;
	if (i==1)
		return V[1].fs*V[1].sc;
	if (dp[i][j]!=-1)
		return dp[i][j];
	dp[i][j]=0;
	dp[i][j]=max(dp[i][j],solve(i-1,j-1)+V[i].fs*V[i].sc);
	dp[i][j]=max(dp[i][j],solve(i-1,j));
	return dp[i][j];
}
int main()
{
	Int T;
	cin>>T;
	for (Int k=1;k<=T;++k)
	{
		V.clear();
		memset(dp,-1,sizeof(dp));
		cin>>N>>K;
		V.pb(mp(0,0));
		for (Int i=1;i<=N;++i)
		{
			Int r,h;
			cin>>r>>h;
			V.pb(mp(r,h));
		}
		sort(V.begin(),V.end());
		double ans=0;
		for (Int i=K;i<=N;++i)
		{
			double tmp=pi*V[i].fs*V[i].fs;
			tmp=tmp+2.00*pi*solve(i-1,K-1);
			tmp=tmp+2.00*pi*V[i].fs*V[i].sc;
			ans=max(ans,tmp);
		}
		printf("Case #%lld: %.7lf\n",k,ans);
	}
	return 0;
}