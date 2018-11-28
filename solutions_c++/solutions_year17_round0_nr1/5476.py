#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define N 1003
ll n, res, t, k, a[N];
string s;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	freopen("test.in", "r", stdin);
	freopen("test.out", "w",stdout);

	cin >> t;
	for (int u = 1; u <= t; u++)
	{
		res = 0;
		cin >> s >> k;
		for (int i = 0; i < s.size(); i++)
			a[i] = (s[i] == '-');
		for (int i = 0; i < s.size();i++)
		{
			if (a[i])
			{
				if (s.size() < k + i)
				{
					res = -1;
					break;
				}
				for (int j = 0; j < k; j++)
					a[i + j] = 1 - a[i + j];
				res++;
			}
		}
		cout << "Case #" << u << ": ";
		if (res < 0)cout << "IMPOSSIBLE";
		else cout << res;
		cout << "\n";
	}
	return 0;
}