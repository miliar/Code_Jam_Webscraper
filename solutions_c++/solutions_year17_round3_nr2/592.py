#include <bits/stdc++.h>
using namespace std;
int done[1500][1500][2][2];
int memo[1500][1500][2][2];
int upto;
pair<int, bool> events[300];
int at[1500];
int dp(int a, int person0, bool p, bool start)
{
	if (a == 1440) {
		if (person0 != 720) return 99999999;
		if (p == start) return 0;
		return 1;
	}
	if (done[a][person0][p][start] == upto) return memo[a][person0][p][start];
	done[a][person0][p][start] = upto;
	if (at[a])
	{
		int even = at[a];
		int add = 0;
		if (events[even].second != p) add++;
		int newperson0 = person0;
		if (!events[even].second)
		{
			newperson0 += events[even].first - a;
		}
		int ans = dp(events[even].first, newperson0, events[even].second, start) + add;
		return memo[a][person0][p][start] = ans;
	}
	int add = 0;
	if (p) add++;
	memo[a][person0][p][start] = dp(a+1, person0+1, 0, start) + add;
	add = 0;
	if (!p) add++;
	return memo[a][person0][p][start] = min(memo[a][person0][p][start], dp(a+1, person0, 1, start) + add);
}
int t, ac, aj;
int main()
{
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		fill_n(at, 1500, 0);
		upto++;
		scanf("%d%d", &ac, &aj);
		for (int j = 1; j <= ac; j++)
		{
			int in1, in2;
			scanf("%d%d", &in1, &in2);
			events[j].first = in2;
			events[j].second = false;
			at[in1] = j;
		}
		for (int j = ac+1; j <= ac+aj; j++)
		{
			int in1, in2;
			scanf("%d%d", &in1, &in2);
			events[j].first = in2;
			events[j].second = true;
			at[in1] = j;
		}
		int ans = min(dp(0, 0, 0, 0), dp(0, 0, 1, 1));
		printf("Case #%d: %d\n", i, ans);
	}
}