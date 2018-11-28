#include <bits/stdc++.h>

#define lli long long int
#define pb push_back
#define pii pair <int, int>
#define pll pair <lli, lli>
#define pdd pair <double, double>
#define _F first
#define _S second
#define mset(x) memset(x, 0, sizeof(x))
#define fastio() ios_base::sync_with_stdio(0)

using namespace std;

double csa(pdd);

const int N = 1005;
pdd DP[N][N];

int main()
{
	int T;
	cin >> T;

	for(int t=1; t<=T; t++)
	{
		int n, k;
		cin >> n >> k;

		// r, h
		vector <pdd> A(n+1);
		for(int i=0; i<n; i++)
			cin >> A[i].first >> A[i].second;

		sort(A.rbegin(), A.rend());

		// csa, max_r
		for(int i=0; i<=n; i++)
			for(int j=0; j<=n; j++)
				DP[i][j] = {0.0, 0.0};

		for(int i=0; i<n; i++)
		{
			for(int h=0; h<=i+1; h++)
			{
				double temp = DP[i][h].first + csa(A[i]);
				double temp_r = max(DP[i][h].second, A[i].first);
				double temp_a = temp + (M_PI * temp_r * temp_r);

				double prev_a = DP[i][h+1].first + (M_PI * DP[i][h+1].second * DP[i][h+1].second);

				if(temp_a > prev_a)
					DP[i+1][h+1] = {temp, temp_r};
				else
					DP[i+1][h+1] = DP[i][h+1];
			}
		}

		double r = DP[n][k].second;
		double ans = DP[n][k].first + (M_PI * r * r);

		printf("Case #%d: ", t);
		cout << fixed << setprecision(10) << ans << endl;
	}

	return (0-0);	
}

double csa(pdd x)
{
	return 2 * M_PI * x.first * x.second;
}