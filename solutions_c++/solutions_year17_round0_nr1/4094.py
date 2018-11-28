#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e3 + 10;

int T, k;
string s;
int a[maxn];

int main ()
{
	cin >> T;
	int t = 0;
	ofstream cout ("out.txt");
	while (T--)
	{
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.size(); ++i)
			if (s[i] == '+')
				a[i] = 1;
			else
				a[i] = 0;

		for (int i = 0; i + k - 1 < s.size(); ++i)
			if (!a[i])
			{
				for (int j = i; j < i + k; ++j)
					a[j] ^= 1;
				++ans;
			}

		for (int i = 0; i < s.size(); ++i)
			if (a[i] != 1)
				ans = -1;

		cout << "Case #" << ++t << ": ";
		if (ans == -1)
			cout << "Impossible\n";
		else
			cout << ans << '\n';
	}
	return 0;
}