#include <bits/stdc++.h>

using namespace std;

#define pi 3.14159265358979323846264338
//3.14159265358979323846
#define neginf -100000000000000000

long double dp[1005][1005];
pair<long double,long double> d[1005];
		
long double recu(int i,int j,int n,int k)
{
	if(j==0)
		return 0.0;
	else if(i>n)
		return neginf;

	if(dp[i][j]!=-1)
		return dp[i][j];

	long double val1 = 2*pi*d[i].first*d[i].second;
	if(j==k)
		val1 = val1 + pi*d[i].first*d[i].first;

	dp[i][j] = max(val1+recu(i+1,j-1,n,k),recu(i+1,j,n,k));

	return dp[i][j];

}

void initialize(int n)
{
	for(int i = 0;i<n+4;i++)
	{
		for(int j=0;j<n+4;j++)
		{
			dp[i][j] = -1;
		}
	}
}	

int main()
{
	int t,tt,i;
	cin >> t;
	for(tt=1;tt<=t;tt++)
	{
		
		int n,k;
		cin >> n >> k;
		initialize(n);
		for(i=1;i<=n;i++)
		{
			cin >> d[i].first >> d[i].second;
		}
		sort(d+1,d+n+1,greater<pair< long double, long double> >());
		long double maxi = 0.0;
		cout << "Case #" << tt << ": ";
		printf("%0.9Lf\n",recu(1,k,n,k));
	}
	return 0;
}