#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll a[20], n, t, x, y, res = 0;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	
	cin >> t;
	for (int u = 1; u <= t; u++)
	{
		memset(a, 0, sizeof a);
		cin >> n;
		x = 0;
		while (n != 0)
		{
			a[x] = n % 10;
			n /= 10;
			x++;
		}

		y = -1;

		for (int i = x - 2; i >= 0; i--)
		if (a[i] < a[i + 1])
		{
			y = i;
			break;
		}
		if (y != -1)
		{
			for (int i = 0; i <= y; i++)
				a[i] = 9;

			for (int i = y + 1; i < x; i++)
			{
				a[i]--;
				if (a[i] < a[i + 1])a[i] = 9;
				else break;
			}
		}
		res = 0;
		for (int i = x; i >= 0; i--)
			res = res * 10 + a[i];
		cout << "Case #" << u << ": " << res << "\n";
	}
	return 0;
}