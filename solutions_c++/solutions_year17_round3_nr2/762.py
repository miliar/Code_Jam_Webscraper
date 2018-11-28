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
Int A[3];
bool v[3][1500];
Int dp[1500][730][3][3];
//Int last=1439;
Int solve(Int i,Int j,Int s,Int l)
{
	if (j>i+1)
		return 1500;
	if (j==0&&l==2)
		return 1500;
	if (v[l][i])
		return 1500;
	if (i==0)
	{
		if (s!=l)
			return 1500;
		if (j==0&&s!=1)
			return 1500;
		if (j==1&&s!=2)
			return 1500;
		return 0;
	}
	if (dp[i][j][s][l]!=-1)
		return dp[i][j][s][l];
	dp[i][j][s][l]=1500;
	//last=i;
	if (l==1)
	{
		dp[i][j][s][l]=min(dp[i][j][s][l],solve(i-1,j,s,l));
		dp[i][j][s][l]=min(dp[i][j][s][l],solve(i-1,j,s,2)+1);
	}
	else
	{
		dp[i][j][s][l]=min(dp[i][j][s][l],solve(i-1,j-1,s,l));
		dp[i][j][s][l]=min(dp[i][j][s][l],solve(i-1,j-1,s,1)+1);
	}
	return dp[i][j][s][l];
}
int main()
{
	Int T;
	cin>>T;
	for (Int k=1;k<=T;++k)
	{
		memset(dp,-1,sizeof(dp));
		memset(v,0,sizeof(v));
		cin>>A[1]>>A[2];
		for (Int i=0;i<A[1];++i)
		{
			Int st,en;
			cin>>st>>en;
			for (Int j=st;j<en;++j)
				v[1][j]=1;
		}
		for (Int i=0;i<A[2];++i)
		{
			Int st,en;
			cin>>st>>en;
			for (Int j=st;j<en;++j)
				v[2][j]=1;
		}
		Int minm=1500;
		//cout<<"Hello\n";
		minm=min(minm,solve(1439,720,1,1));
		//cout<<"Hello2\n";
		minm=min(minm,solve(1439,720,1,2)+1);
		minm=min(minm,solve(1439,720,2,1)+1);
		minm=min(minm,solve(1439,720,2,2));
		printf("Case #%lld: %lld\n",k,minm);
	}
	return 0;
}