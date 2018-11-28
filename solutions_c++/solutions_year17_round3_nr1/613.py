#include <bits/stdc++.h>

#define MAX 1010
#define INF 0x3f3f3f3f
using namespace std;
typedef long long ll;
const double pi = acos(-1);

int t,n,k,h,r,m;
vector<pair<double,double> > pan;
double dp[MAX][MAX];
int mark[MAX][MAX];

double sqr(double x)
{
	return x * x;
}

double solve(int curr, int k)
{
	if (curr == n)
	{
		if (m == k)
			return 0;
		return -10000000000000000.0;
	}

	double & ret = dp[curr][k];
	if (mark[curr][k])
		return ret;
	mark[curr][k] = 1;
	ret = 0;
	if (k == 0)
	{
		ret = solve(curr + 1, k + 1) + pi * sqr(pan[curr].first) + 2.0 * pi * pan[curr].first * pan[curr].second;
		ret = max(ret, solve(curr + 1, k));
	}
	else
	{
		ret = solve(curr + 1, k + 1) + 2.0 * pi * pan[curr].first * pan[curr].second;
		ret = max(ret, solve(curr + 1, k));
	}
	return ret;
}

int main()
{
	scanf("%d",&t);
	for (int cases = 1; cases <= t; ++cases)
	{
		memset(mark, 0, sizeof mark);
		scanf("%d%d", &n, &m);
		pan.clear();
		for (int i = 0; i < n; ++i)
		{	
			scanf("%d%d",&r,&h);
			pan.push_back(make_pair(r, h));
		}
		sort(pan.rbegin(), pan.rend());
		printf("Case #%d: %.8lf\n", cases, solve(0, 0));
	}
	return 0;
}