#include <bits/stdc++.h>

#define ll long long
#define ld long double

#define all(x) x.begin(),x.end()

using namespace std;

int n,q;
int e[100],s[100];
ld d[100][100];
int u[100],v[100];

ld sum[100];

ld dp[100][100];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cout<<fixed<<setprecision(10);

    int testno;
    cin>>testno;
    for(int testi=1; testi<=testno; testi++)
    {

    	cin>>n>>q;
    	for (int i=0; i<n; i++)
    		cin>>e[i]>>s[i];
    	for (int i=0; i<n; i++)
    		for (int j=0; j<n; j++)
    			cin>>d[i][j],dp[i][j] = 1e12;
		for (int i=0; i<q; i++)
			cin>>u[i]>>v[i];

        sum[0] = 0;
		for (int i=1; i<n; i++)
			sum[i] = sum[i-1]+d[i-1][i];

    	dp[0][0] = 0;
    	for (int i=0; i+1<n; i++)
    	{
    		for (int j=0; j<=i; j++)
    		{
    			dp[i][i] = min(dp[i][i],dp[i][j]);
	    		if (sum[i+1]-sum[j] <= e[j])
	    			dp[i+1][j] = min(dp[i+1][j],dp[i][j] + d[i][i+1]/s[j]);
	    	}
    	}

    	ld r = 1e12;
    	for (int i=0; i<n; i++)
    		r = min(r,dp[n-1][i]);

    	cout<<"Case #"<<testi<<": ";
    	cout<<r;
    	cout<<'\n';

    	cerr<<"Case #"<<testi<<": ";
    	cerr<<r;
    	cerr<<'\n';
    }

    return 0;
}

