#include <iostream>
#include <vector>
#include <string>

using namespace std;

char flip(char c)
{
	return c == '-' ? '+' : '-';
}

void solve()
{
	string s;
	cin >> s;
	int n = s.size(), i;
	for (i = 1; i < n; ++i)
	{
		if (s[i] < s[i - 1])
			break;
	}
	if (i < n)
	{
		--i;
		while (i > 0 && s[i] == s[i - 1])
			--i;
		--s[i];
		for (++i; i < n; ++i)
			s[i] = '9';
	}
	for (i = 0; i < n - 1 && s[i] == '0'; ++i);
	s = s.substr(i);
	cout << s << endl;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
}