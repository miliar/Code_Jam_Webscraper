#include <bits/stdc++.h>

using namespace std;

void solve()
{
	string s;
	int k;
	cin >> s >> k;
	string ts = s;
	int n = s.size();
	int i = 0;
	while(true)
	{
		int p = s.find('-');
		if(p == string::npos)
		{
			cout << i << '\n';
			break;
		}
		if(p + k > n)
		{
			cout << "IMPOSSIBLE" << '\n';
			break;
		}
		for(int j = 0; j < k; j++)
			s[p + j] = (s[p + j] == '+' ? '-' : '+');
		i++;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
