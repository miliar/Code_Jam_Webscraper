#include <iostream>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <string>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;
string s;
int n, k;

int main()
{
	int t;

	cin >> t;
	for (int o = 1; o <= t; ++o)
	{
		cin >> s;
		n = s.size();
		cin >> k;
		long long ans = 0;
		for (int i = 0; i <= n - k; ++i)
		{
			int tmp = i + k;
			if(s[i] == '+')
				continue;
			ans++;
			for (int j = i; j < i + k; ++j)
			{
				if(s[j] == '-')
					s[j] = '+';
				else
				{
					tmp = min(tmp, j);
					s[j] = '-';
				}
			}
			i = tmp - 1;
		}
		bool fl = false;
		for (int i = 0; i < n; ++i)
		{
			if(s[i] != '+')
			{
				fl = true;
				break;
			}
		}
		if(fl)
			cout << "Case #" << o << ": " << "IMPOSSIBLE\n";
		else
			cout << "Case #" << o << ": " << ans << endl;

	}
	return 0;
}
