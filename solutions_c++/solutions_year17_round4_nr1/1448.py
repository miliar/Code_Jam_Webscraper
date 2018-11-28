#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define MAX 101
using namespace std;
int dp[101][101][101][101][4];
int mark[101][101][101][101][4];
int t,n,p,v[MAX];
int cases;

int solve(int qnt0, int qnt1, int qnt2, int qnt3, int l)
{
	if (qnt0 < 0 or qnt1 < 0 or qnt2 < 0 or qnt3 < 0)
		return -INF;
	if (qnt0 == 0 and qnt1 == 0 and qnt2 == 0 and qnt3 == 0)
	{
		return 0;
	}
	int & ret = dp[qnt0][qnt1][qnt2][qnt3][l];
	if (mark[qnt0][qnt1][qnt2][qnt3][l] == cases)
		return ret;
	mark[qnt0][qnt1][qnt2][qnt3][l] = cases;
	ret = solve(qnt0 - 1, qnt1, qnt2, qnt3, (p - l)%p) + (l == 0);
	ret = max(ret, solve(qnt0, qnt1 - 1, qnt2, qnt3, (p - (1 - l + p)%p)%p) + (l == 0));
	ret = max(ret, solve(qnt0, qnt1, qnt2 - 1, qnt3, (p - (2 - l + p)%p)%p) + (l == 0));
	ret = max(ret, solve(qnt0, qnt1, qnt2, qnt3 - 1, (p - (3 - l + p)%p)%p) + (l == 0));
	return ret;
}


int main()
{
	ios :: sync_with_stdio(false);
	cin >> t;
	memset(dp, -1, sizeof dp);
	memset(mark, 0, sizeof mark);
	for (cases = 1; cases <= t; ++cases)
	{
		cin >> n >> p;
		int qnt[4];
		memset(qnt, 0, sizeof qnt);
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i];
			qnt[v[i]%p]++;
		}
		cout << "Case #" << cases << ": " << solve(qnt[0], qnt[1], qnt[2], qnt[3], 0) << "\n";
	}
	return 0;

}