#include <bits/stdc++.h>
using namespace std;

int T;
long long n;

int dp[20][10][2];
vector < int > Dec;

int f (int pos, int digit, int smaller)
{
	if (dp[pos][digit][smaller] == -1)
	{
		if (pos == Dec.size())
			return (dp[pos][digit][smaller] = 1);

		dp[pos][digit][smaller] = 0;
		
		int st = (smaller) ? (9) : (Dec[pos]);

		for (int i = st; i >= digit; i--)
			dp[pos][digit][smaller] |= f (pos + 1, i, (smaller | (i < Dec[pos])));
	}

	return dp[pos][digit][smaller];
}

int main ()
{
	ofstream cout ("out.txt");
	scanf ("%d", &T);

	int t = 0;

	while (T--)
	{
		scanf ("%lld", &n);

		Dec.clear();
		while (n > 0)
		{
			Dec.push_back (n % 10);
			n /= 10;
		}

		long long ans = 0;

		reverse (Dec.begin(), Dec.end());

		memset (dp, -1, sizeof (dp));

		f(0, 0, 0);

		int digit = 0;
		int smaller = 0;

		for (int pos = 0; pos < Dec.size(); pos++)
		{
			int st = (smaller) ? (9) : (Dec[pos]);
			for (int i = st; i >= digit; i--)
				if (f (pos + 1, i, (smaller | (i < Dec[pos]))))
				{
					ans = ans * 10 + i;
					digit = i;
					smaller |= (i < Dec[pos]);
					break;
				}
		}

		cout << "Case #" << ++t << ": " << ans << '\n';
	}

	return 0;
}