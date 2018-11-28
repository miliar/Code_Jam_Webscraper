#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __int("$3");

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		string s;
		int k;
		cin >> s >> k;
		int n = s.length();
		int d = 0;
		for (int j = 0; j <= n - k; ++j)
		{
			if (s[j] == '-')
			{
				++d;
				for (int l = 0; l < k; ++l)
				{
					if (s[j+l] == '+')
					{
						s[j+l] = '-';
					}
					else
					{
						s[j+l] = '+';
					}
				}
			}
		}
		for (int j = n - k; j < n; ++j)
		{
			if (s[j] != '+')
			{
				d = -1;
				break;
			}
		}
		cout << "Case #" << i << ": ";
		if (d == -1)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << d << endl;
		}
	}
	return 0;
}
