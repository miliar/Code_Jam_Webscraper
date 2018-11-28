/*
СТРОИМ СТЕНУ РАБОТЯГИ!
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define zhfs main
#define mp(a, b) make_pair(a, b)
#define fi first
#define se second
#define re return
#define forn(i, n) for (int i = 1; i <= n; i++)
bool check(string s, string t)
{
	while (s.length() < t.length()) s += s.back();
	return s <= t;
}
int zhfs()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		string s;
		cin >> s;
		string tmp;
		for (int i = 0; i < (int)s.length(); i++)
		{
			tmp += "1";
		}
		if (tmp > s)
		{
			printf("Case #%d: ", tt);
			for (int i = 0; i < (int)s.length() - 1; i++)
			{
				printf("9");
			}
			printf("\n");
		}
		else
		{
			string res;
			for (int i = 0; i < (int)s.length(); i++)
			{
				res += '1';
				int go = -1;
				for (int j = 0; j < 10; j++)
				{
					res[i] = j + '0';
					if (check(res, s)) go = j;
				}
				res[i] = go + '0';
			}
			printf("Case #%d: ", tt);
			for (int j = 0; j < (int)res.length(); j++)
			{
				printf("%c", res[j]);
			}
			printf("\n");
		}
	}
}

