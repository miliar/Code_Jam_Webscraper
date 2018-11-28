#include "bits/stdc++.h"

using namespace std;

int dp[2][20][10];
std::vector<int> v;
long long ansis = -1;
int temp[20];
long long rec(int len, int digit, int equal)
{
//	printf("ASDF SDFASFS %d %d %d\n",len,digit,equal);
	if(len == 0)
	{
//		printf("HASDG %d %d\n", temp[len+1], temp[len]);
	}
	if(len == -1 && ansis == -1)
	{
///		printf("PPPPPPP\n");
		long long tempv = 1;
		ansis = 0;
		for(int i = 0 ; i < 19 ; i++)
		{
			ansis += temp[i] * tempv;
			tempv *= 10;
		}
	}
	if(len == -1)
		return 1;
//	printf("HHHHH f %lld\n",dp[equal][len][digit]);
	if(dp[equal][len][digit] != -1)
		return dp[equal][len][digit];
//	printf("HHHHH123\n");
	dp[equal][len][digit] = 0;
	if(equal)
	{
//		printf("QQQQQQ");
		for(int start = v[len] ; start >= digit ; start--)
		{
			temp[len] = start;
			dp[equal][len][digit] += rec( len - 1 , start , equal && (start == v[len]));
		}
	}
	else
	{
//		printf("Going %d\n");
		for(int start = 9 ; start >= digit ; start--)
		{

			temp[len] = start;
			dp[equal][len][digit] += rec(len - 1, start, 0);
		}
	}
	return dp[equal][len][digit];
}


long long  solve()
{
	long long N;
	cin >> N;
	memset(dp,-1,sizeof(dp));
	int times = 20;
	v.clear();
	long long tN = N;
	while(times--)
	{
		v.push_back(tN % 10);
		tN /= 10;
	}
	ansis = -1;
	rec(19, 0, 1);

}

int main()
{
	int T,testCase;
	scanf("%d",&T);
	testCase = T;
	while(T--)
	{
		solve();
		printf("Case #%d: %lld\n",testCase - T, ansis);
	}
}