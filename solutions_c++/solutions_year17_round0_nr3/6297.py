#include <iostream>

using namespace std;


const int MAXN = 1000 * 1000 + 10;

long long dp[MAXN];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		long long n, k;
		cin >> n >> k;
		long long lo = 1, hi = n + 1;
		while (hi - lo > 1)
		{
			long long mid = (lo + hi) / 2;
			for (int i = 0; i < mid; i++)
				dp[i] = 0;
			for (int i = mid; i <= n; i++)
				dp[i] = dp[(i - 1) / 2] + dp[i / 2] + 1;
			if (dp[n] >= k)
				lo = mid;
			else
				hi = mid;
		}
		cout << "Case #" << tc << ": " << lo / 2 << " " << (lo - 1) / 2 << endl;
	}
}
