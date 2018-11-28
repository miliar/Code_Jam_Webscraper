#include <bits/stdc++.h>
#define debug(x) cout << #x << " = (" << x << ")\n"
using namespace std;
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t; cin >> t;
	for(int tc = 1; tc <= t; tc++)
	{
		string s; cin >> s;
		int pos = -1;
		for(int i = 0; i + 1 < s.size(); i++)
		{
			if (s[i] > s[i + 1])
			{
				pos = i; break;
			}
		}
		if (pos >= 0)
		{
			for(int i = pos; i >= 0; i--)
			{
				if (s[i] == '0') s[i] = '9';
				else s[i]--;

				for(int j = i + 1; j < s.size(); j++)
					s[j] = '9';

				if (i > 0 && s[i - 1] <= s[i]) break;
			}

			int i;
			for(i = 0; i < s.size() && s[i] == '0'; i++);
			if (i == s.size()) s = "0";
			else s = s.substr(i, -1);
		}
		cout << "Case #" << tc << ": " << s << "\n";
	}
	return (0);
}

