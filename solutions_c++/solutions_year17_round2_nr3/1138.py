#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define cerr while(0)cerr
int main()
{
	ios::sync_with_stdio(0);
	long long T;
	cin>>T;
	for (long long t = 1; t <= T; ++t)
	{
		long long N, Q;
		cin>>N>>Q;
		long long e[N], s[N];
		for (long long i = 0; i < N; ++i)
		{
			cin>>e[i]>>s[i];
		}
		long long d[N][N];
		for (long long i = 0; i < N; ++i)
		{
			for (long long j = 0; j < N; ++j)
			{
				cin>>d[i][j];
			}
		}
		long long dist[N+1];
		dist[0] = 0;
		for (long long i = 1; i < N; ++i)
		{
			dist[i] = dist[i-1] + d[i-1][i];
			cerr<<dist[i]<<' ';
		}
		cerr<<'\n';
		long long x;
		cin>>x>>x;
		long double dp[N+1][N+1];
		long double mindp[N+1];
		for (long long i = 0; i <= N; ++i)
		{
			mindp[i] = DBL_MAX;
		}
		memset(dp, 0, sizeof dp);
		for (long long i = 1; i < N; ++i)
		{
			for (long long j = 0; j < i; ++j)
			{
				cerr<<i<<' '<<j<<":\n";
				long long distance = dist[i];
				if (j > 0) distance -= dist[j];

				if (distance <= e[j])
				{
					cerr<<"yes\n";
					dp[i][j] = distance;
					dp[i][j] /= s[j];

					if (j > 0)
					{
						dp[i][j] += mindp[j];
					}
				}
				else
				{
					dp[i][j] = DBL_MAX;
				}
				cerr<<distance<<' '<<dp[i][j]<<'\n';
				mindp[i] = min(mindp[i], dp[i][j]);
			}
		}

		cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<mindp[N-1]<<'\n';
	}
}