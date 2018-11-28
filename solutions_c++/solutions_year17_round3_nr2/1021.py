#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
using ll = long long;
#define INF 1000000
#define NMAX 1441
#define VMAX 721

int dp[2][NMAX][VMAX][2];
bool ok[2][NMAX];

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	#endif

	int n, ans, aux, t, tt, f, i, j, last;
	int ac, aj, c, d;

	cin >> t;
	for(tt = 1; tt <= t; ++tt)
	{
		for(f = 0; f < 2; ++f)
			for(i = 0; i < NMAX; ++i)
				ok[f][i] = true;

		cin >> ac >> aj;
		while(ac--)
		{
			cin >> c >> d;
			for(; c < d; ++c) ok[0][c] = false;
		}

		while(aj--)
		{
			cin >> c >> d;
			for(; c < d; ++c) ok[1][c] = false;
		}

		for(f = 0; f < 2; ++f)
		{
			for(i = 0; i < NMAX; ++i)
				for(j = 0; j < VMAX; ++j)
					for(last = 0; last < 2; ++last)
						dp[f][i][j][last] = INF;

			dp[f][1][1][f] = (ok[f][0] ? 0 : INF);

			for(i = 2; i < NMAX; ++i)
				for(j = 0; j <= i && j < VMAX; ++j)
					for(last = 0; last < 2; ++last)
					{
						// calc dp[f][i][j][last]
						aux = INF;
						if(ok[last][i - 1])
						{
							if(j >= (last == f)) aux = min(aux, dp[f][i - 1][j - (last == f)][last]);
							if(j >= (last == f)) aux = min(aux, dp[f][i - 1][j - (last == f)][last ^ 1] + 1);
						}

						//if(f == 0 && i == 2 && j == 2 && last == 1) cerr << "aux = " << aux << '\n';
						dp[f][i][j][last] = aux;
					}
		}

		//cerr << dp[0][1][2][1] << '\n';

		for(ans = INF, f = 0; f < 2; ++f)
			for(last = 0; last < 2; ++last)
				ans = min(ans, dp[f][NMAX - 1][VMAX - 1][last] + (f != last));

		cout << "Case #" << tt << ": " << ans << '\n';
	}

	return 0;
}