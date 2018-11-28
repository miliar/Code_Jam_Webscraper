#include <bits/stdc++.h>

using namespace std;

int t, tt;

int main()
{
	cin >> t;
	while (t--)
	{
		string s;
		int k, ans = 0;
		cin >> s >> k;
		int len = s.length();
		for (int i = 0; i < len; i++)
		{
			if (s[i] == '-')
			{
				if (i + k - 1 >= len)
				{
					ans = -1;
					break;
				}
				else
				{
					ans++;
					for (int j = i; j < i + k; j++)
					{
						char newChar = '-';
						if (s[j] == '-')
							newChar = '+';
						s[j] = newChar;
					}
				}
			}
		}
		cout << "Case #" << ++tt << ": ";
		if (ans != -1)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}	
	return 0;
}