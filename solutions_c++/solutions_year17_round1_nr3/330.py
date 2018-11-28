#include<cstdio>
#include<algorithm>
#include<cstring>

const int INF=1000000;

int t;

int hd,ad,hk,ak,b,d;
int dp[110][110][110][110];

int solve(int hi,int ai,int hj,int aj)
{
	if(hj<=ai) return 1;
	if(hi<=0) return INF;

	if(dp[hi][ai][hj][aj]<0)
	{
		int A,B,C,D;
		A=(hi-aj>0)?solve(hi-aj,ai,hj-ai,aj):INF; //attack
		B=(hi-aj>0&&b>0)?solve(hi-aj,ai+b,hj,aj):INF; //buff
		C=(hd-aj>0&&hd-aj>hi)?solve(hd-aj,ai,hj,aj):INF; //cure
		D=(hi-std::max(0,aj-d)>0&&d>0&&aj>0)?solve(hi-std::max(0,aj-d),ai,hj,std::max(0,aj-d)):INF; //debuff
		dp[hi][ai][hj][aj]=std::min(std::min(A,B),std::min(C,D))+1;
//		if(A<C) printf("dp[%d][%d][%d][%d]=dp[%d][%d][%d][%d]+1=%d\n",hi,ai,hj,aj,hi-aj,ai,hj-ai,aj,dp[hi][ai][hj][aj]);
//		else printf("dp[%d][%d][%d][%d]=dp[%d][%d][%d][%d]+1=%d\n",hi,ai,hj,aj,hd-aj,ai,hj,aj,dp[hi][ai][hj][aj]);
	}
	return dp[hi][ai][hj][aj];
}

int main()
{
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small-attempt0.out","w",stdout);

	scanf("%d",&t);
	for(int test_case=1;test_case<=t;test_case++)
	{
		memset(dp,-1,sizeof(dp[0][0][0][0])*110*110*110*110);

		scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);

		printf("Case #%d: ",test_case);
		int A=solve(hd,ad,hk,ak);
		if(A>=INF) printf("IMPOSSIBLE\n");
		else printf("%d\n",A);
	}
	return 0;
}
