#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <map>
#include <cmath>
#include <iomanip>

using namespace std;

int t, n, q, a;
pair<double, double> ar[100];
double dp[102], dist[102], sum[102];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	for(int z=1; z<=t; z++)
	{
		cin>>n>>q;
		for(int i=0; i<n; i++) cin>>ar[i].first>>ar[i].second;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<n; j++)
			{
				cin>>a;
				if(j==i+1) dist[j]=a;
			}
		}
		sum[0]=0;	
		for(int i=1; i<n; i++) sum[i]=dist[i]+sum[i-1];
		cin>>a>>a;
		for(int i=0; i<=n; i++) dp[i]=1e18;
		dp[0]=0;
		for(int i=1; i<n; i++)
		{
			for(int j=i-1; j>=0;  j--)
			{
				if(sum[i]-sum[j]>ar[j].first) continue;
				dp[i]=min(dp[i], dp[j]+(sum[i]-sum[j])/ar[j].second);
			}
		}
		cout<<fixed<<"Case #"<<z<<": "<<dp[n-1]<<endl;
	}
	return 0;
}