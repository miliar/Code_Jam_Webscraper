#include <bits/stdc++.h>

using namespace std;

int t, k;
string s;

int main(void)
{
	ios :: sync_with_stdio(false);
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> s >> k;
		int ans = 0;
		for (int j = 0; j + k <= s.size(); ++j)
		{
			if (s[j] == '-')
			{
				ans++;
				for (int a = j; a < j + k; ++a)
				{
					if (s[a] == '-')
						s[a] = '+';
					else
						s[a] = '-';
				}
			}
		}
		for (int j = 0; j < s.size(); ++j)
		{
			if (s[j] == '-')
				ans = -1;
		}
		if (ans == -1)
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
		else
			cout << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}
