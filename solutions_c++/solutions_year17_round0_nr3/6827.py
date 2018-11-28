#include <bits/stdc++.h>

using namespace std;


void solve()
{
	int n, k;
	cin >> n >> k;
	bool used[n + 2];
	fill(used, used + n + 2, 0);
	used[0] = used[n + 1];
	int ls[n + 2], rs[n + 2];
	for(int i = 1; i <= n; i++)
	{
		ls[i] = i;
		rs[n - i + 1] = i;
	}
	for(int i = 1; i <= k; i++)
	{
		int c = -1;
		for(int j = 1; j <= n; j++)
			if(used[j] == 0 && (c == -1 || make_pair(min(ls[j], rs[j]), max(ls[j], rs[j])) > make_pair(min(ls[c], rs[c]), max(ls[c], rs[c]))))
				c = j;
		used[c] = 1;
		if(i == k)
			cout << max(ls[c], rs[c]) - 1 << ' ' << min(ls[c], rs[c]) - 1 << endl;
		for(int j = 1; j <= n; j++)
		{
			if(j > c)
				ls[j] = min(ls[j], j - c);
			else
				rs[j] = min(rs[j], c - j);
		}
	}
	
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
