#include <iostream>
#include <sstream>
#include <set>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;


ll solve(ll n)
{
	bool fl = true;
	ll res = n;
	while (fl)
	{
		fl = false;
		stringstream ss;
		ss << res;
		string s;
		ss >> s;
		for (int i = 1; i < s.size(); ++i)
		{
			if (s[i] < s[i - 1])
			{
				fl = true;
				s[i - 1]--;
				for (int j = i; j < s.size(); ++j)
					s[j] = '9';
			}
		}
		ss.clear();
		ss << s;
		ss >> res;
	}
	return res;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("a.out", "w+", stdout);
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t)
	{
		ll n;
		cin >> n;
		ll res = solve(n);
		printf("Case #%d: ", t);
		cout << res;
		printf("\n");
	}
	return 0;
}