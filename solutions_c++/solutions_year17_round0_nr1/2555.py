#include <iostream>
#include <set>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

typedef long long ll;

char flip(char c)
{
	return c == '+' ? '-' : '+';
}

ll solve(string s, int k)
{
	ll res = 0;
	for (int i = 0; i < s.size() - k + 1; ++i)
	{
		if (s[i] == '-')
		{
			res++;
			for (int j = i; j < i + k; ++j)
				s[j] = flip(s[j]);
		}
	}
	for (int i = 0; i < s.size(); ++i)
		if (s[i] == '-')
			return -1;
	return res;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w+", stdout);
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		ll res = solve(s, k);
		printf("Case #%d: ", t);
		if (res < 0)
			cout << "IMPOSSIBLE";
		else
			cout << res;
		printf("\n");
	}
	return 0;
}