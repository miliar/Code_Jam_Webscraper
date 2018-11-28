#include<iostream>
using namespace std;
#define fs first
#define sc second
#define MAX 100000
#define pb push_back
#define mp make_pair
#define INF 1000000000000
#define MOD 1000000007
#define eps 0.000000001
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
Int E[200],S[200],N;
double dp[200][200];
Int D[200];
double solve(Int i,Int j)
{
	if (dp[i][j]+1>eps)
		return dp[i][j];
	if (D[i]-D[j]>E[j])
		return dp[i][j]=INF;
	if (j==1)
		return dp[i][j]=(D[i]-D[j])*1.00/S[j];
	dp[i][j]=INF;
	for (Int k=1;k<j;++k)
		dp[i][j]=min((D[i]-D[j])*1.00/S[j]+solve(j,k),dp[i][j]);
	return dp[i][j];
}
int main()
{
	Int T;
	cin>>T;
	for (Int k=1;k<=T;++k)
	{
		memset(dp,-1,sizeof(dp));
		memset(D,0,sizeof(D));
		Int N,Q,u,v;
		cin>>N>>Q;
		for (Int i=1;i<=N;++i)
			cin>>E[i]>>S[i];
		for (Int i=1;i<=N;++i)
		{
			for (Int j=1;j<=N;++j)
			{
				Int d;
				cin>>d;
				if (j==i+1)
					D[j]=d;
			}
		}
		cin>>u>>v;
		for (Int i=2;i<=N;++i)
			D[i]+=D[i-1];
		double minm=INF;
		for (Int i=1;i<N;++i)
			minm=min(minm,solve(N,i));
		printf("Case #%lld: %lf\n",k,minm);
	}
	return 0;
}
