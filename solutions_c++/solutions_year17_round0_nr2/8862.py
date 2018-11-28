#include <bits/stdc++.h>

using namespace std;

bool is_tidy(int n)
{
	stringstream ss;
	ss << n;
	string s = ss.str();
	for(int i = 1; i < s.size(); i++)
		if(s[i] < s[i - 1])
			return 0;
	return 1;
}

void solve()
{
	int n;
	cin >> n;
	int ans = 0;
	for(int i = 1; i <= n; i++)
		if(is_tidy(i))
			ans = i;
	cout << ans << endl;
}

signed main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
