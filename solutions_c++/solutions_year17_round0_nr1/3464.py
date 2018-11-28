#include <bits/stdc++.h>

using namespace std;

int T;
int k;
bool a[1024];
string s;

int main()
{
	cin >> T;

	for (int C = 1; C <= T; C++)
	{
		int ans = 0;
		cin >> s >> k;
		for (int i = 0; i < s.size() - k + 1; i++)
		{
			if (s[i] == '-')
			{
				ans++;
				for (int j = i; j < i + k; j++)
				{
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		cout << "Case #" << C << ": ";
		if (all_of(s.begin(), s.end(), [](char c){ return c == '+'; }))
			cout << ans << '\n';
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}
