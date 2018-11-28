#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
#define x first
#define y second

int seat[1005][2];
int total[2];/*
pii count_most(int which)
{
	pii res(-1, -1);
	int last = -1, cnt = 0;
	for (int i = 0; i < (int)t[which].size(); i++)
	{
		if (t[which][i] == last)
			cnt++;
		else
		{
			last = t[which][i];
			cnt = 1;
		}
		res = max(res, pii(cnt, last));
	}
	return res;
}*/

pii sol()
{
	int n, m, c;
	cin >> n >> c >> m;
	memset(seat, 0, sizeof seat);
	total[0] = total[1] = 0;
	for (int i = 1; i <= m; i++)
	{
		int pi, bi;
		cin >> pi >> bi;
		seat[pi][bi - 1]++;
		total[bi - 1]++;
	}
	cerr << total[0] << ' ' << total[1] << endl;
	pii ans(max(total[0], total[1]), 0);
	int c1 = 0, c2 = 0;
	for (int i = 1; i <= n; i++)
	{
		if (seat[i][0] > seat[c1][0]) c1 = i;
		if (seat[i][1] > seat[c2][1]) c2 = i;
	}
	int ans2 = 0;
	if (seat[c1][0] + seat[c1][1] > ans.first)
	{
		if (c1 == 1) return pii(seat[c1][0] + seat[c1][1], 0);
		else ans2 = max(ans2, seat[c1][0] + seat[c1][1] - ans.first);
	}
	if (seat[c2][0] + seat[c2][1] > ans.first)
	{
		if (c2 == 1) return pii(seat[c2][0] + seat[c2][1], 0);
		else
			ans2 = max(ans2, seat[c2][0] + seat[c2][1] - ans.first);
	}
	ans.second = ans2;
	return ans;
}

int main()
{
//	freopen("B-small-attempt0.in", "r", stdin);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		pii tans = sol();
		printf("Case #%d: %d %d\n", i, tans.x, tans.y);
	}
	return 0;
}

// solve small
