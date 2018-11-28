#include <bits/stdc++.h>
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define pi pair <int, int>
#define ppi pair <pair <int, int>, int>
#define fi first
#define se second
typedef long long ll;

using namespace std;

ll a[105], b[105], c[105][105], d[105][105];
double dp[105];
int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	freopen("pony.in", "r", stdin);
	freopen("pony.out", "w", stdout);

	ll t=1, i, l, j, m, p, n;
	cin>>t;
	for(l=1; l<=t; l++)
	{
		for(i=0; i<105; i++)
			dp[i]=0;
		cin>>n>>i;
		for(i=1; i<=n; i++)
			cin>>a[i]>>b[i];
		for(i=1; i<=n; i++)
		{
			for(j=1; j<=n; j++)
				cin>>c[i][j];
		}

		
		cin>>i>>i;
		for(i=1; i<=n; i++)
        {
        	for(j=i+1; j<=n; j++)
        	{
        		d[i][j]=d[i][j-1]+c[j-1][j];
        	}
        }
		dp[1]=0;

        for(i=2; i<=n; i++)
        {
        	dp[i]=1e18;
        	for(j=1; j<i; j++)
        	{

        		if(a[j]>=d[j][i])
        		{
        			dp[i]=min(dp[i],dp[j]+((1.0*d[j][i])/b[j]));
        		}
        	}
        }

		printf("Case #%lld: %0.8f\n", l, dp[n]);


	}

	return 0;
}