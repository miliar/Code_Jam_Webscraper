#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAXN = 100500;

void sol()
{
	string s;
	int k;
	int ans = 0;
	cin >> s >> k;
	for (int i = 0; i < (int)s.size() - k + 1; i++)
	{
		if (s[i] == '-')
		{
			ans++;
			for (int j = 0; j < k; j++)
				s[i + j] ^= '-' ^ '+';
		}
	}
	for (int i = 0; i < (int)s.size(); i++)
	{
		if (s[i] == '-')
		{
			cout << "IMPOSSIBLE\n";
			return;
		}
	}
	cout << ans << '\n';
}

int main()
{                                                     
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		sol();
	}
	
	return 0;
}

