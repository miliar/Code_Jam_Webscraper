#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define F first
#define S second
#define all(v) v.begin(),v.end()
#define make0(a) memset(a,0,sizeof(a))
#define make1(a) memset(a,-1,sizeof(a))

const int mod = 1e9+7;

int main()
{
	int T;
	cin >> T;
	for(int f=1;f<=T;f++)
	{
		ll N,Q;
		cin >> N >> Q;
		pair <double,double> A[N];
		for(int i=0;i<N;i++)
			cin >> A[i].F >> A[i].S;
		double D[N][N];
		double dist[N];
		dist[0] = 0;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				cin >> D[i][j];
				if(j == i+1)
				{
					dist[i+1] = D[i][j];
					if(i)
						dist[i+1] += dist[i];
				}
			}
		}
		int x;
		cin >> x >> x;
		double dp[N];
		for(int i=0;i<N;i++)
			dp[i] = 1e19;
		dp[0] = 0;
		for(int i=1;i<=N-1;i++)
		{
			for(int j=0;j<i;j++)
			{
				if(dist[i] - dist[j] > A[j].F)
					continue;
				double diff = dist[i] - dist[j];
				dp[i] = min(dp[i], dp[j] + diff/A[j].S);
			}
		}
		printf("Case #%d: %.6lf\n",f,dp[N-1]);
	}
	return 0;
}