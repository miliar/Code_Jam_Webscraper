#include <iostream>
#include <vector>
#include <string>

using namespace std;

char flip(char c)
{
	return c == '-' ? '+' : '-';
}

void solve()
{
	int k;
	string s;
	cin >> s >> k;
	int cnt = 0, n = s.size();
	for(int i = 0; i + k <= n; ++i)
		if (s[i] == '-')
		{
			++cnt;
			for (int j = 0; j < k; ++j)
				s[i + j] = flip(s[i + j]);
		}
	for(int i = 0; i < n; ++i)
		if (s[i] != '+')
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	cout << cnt << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
}