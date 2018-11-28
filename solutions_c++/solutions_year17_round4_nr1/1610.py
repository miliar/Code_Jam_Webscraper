#include <bits/stdc++.h>
using namespace std;
int n, p, g;
int cnt[4];
int sol()
{
	cin >> n >> p;
	memset(cnt, 0, sizeof cnt);
	for (int i = 0; i < n; i++)
	{
		int t;
		cin >> t;
		cnt[t % p]++;
	}
	if (p == 2) {return cnt[0] + (cnt[1] + 1) / 2;}
	else if (p == 3) {
		int tmin = min(cnt[1], cnt[2]);
		cnt[1] -= tmin;
		cnt[2] -= tmin;
		return cnt[0] + tmin + (max(cnt[1], cnt[2]) + 2) / 3;
	} else if (p == 4)
	{
		int tmin = min(cnt[3], cnt[1]);
		cnt[3] -= tmin;
		cnt[1] -= tmin;
		int ans = cnt[0] + tmin;
		ans += cnt[2] / 2 + cnt[2] % 2;
		cnt[2] %= 2;
		if (cnt[2] && cnt[1] >= 2) cnt[1] -= 2;
		else cnt[1] = 0;
		ans += (cnt[1] + 3) / 4;
		return ans;
	}
}
int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: %d\n", i, sol());
	}
	return 0;
}
