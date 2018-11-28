#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		vector<int> kek;
		int cur = 0;
		int pt = 0;
		int ans = 0;
		for (int j = 0; j < s.size(); ++j)
		{
			while (pt < kek.size() && kek[pt] == j)
				++pt, cur ^= 1;
			if (int(s[j] == '-') ^ cur)
			{
				if (j + k <= s.size())
				{
					cur ^= 1, ++ans, kek.push_back(j + k);
				}
				else
				{
					ans = -1;
					break;
				}
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (ans == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}

}
