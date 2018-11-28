#include <bits/stdc++.h>
#define ll long long
#define int long long
#define M 1000000007
using namespace std;

int powi(int base,int exp)
{
	int res=1;
	while(exp)
	{
		if(exp%2)res*=base;
		base*=base;
		exp/=2;
	}
	return res;
}

main()
{
	freopen("output.txt","w",stdout);
	freopen("input.txt","r",stdin);
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;

	for(int test=1;test<=t;test++)
	{
		int dp[10][20];

		int n;
		cin>>n;

		int len=0,arr[20];
		for(int i=n;i;i/=10,len++)
		{
			arr[len]=i%10;
		}
		
		for(int i=0;i<=9;i++)
		{
			dp[i][len]=0;
		}

		for(int i=len-1;i>=0;i--)
		{
			for(int j=0;j<=9;j++)
			{
				dp[j][i]=9*powi(10,len-i-1)+dp[j][i+1];
			}
		}

		int prev=0,st=0,ans=0;
		bool fg=1;
		for(int i=len-1;i>=0;i--)
		{
			if(arr[i]<st)
			{
				fg=0;
				break;
			}

			for(int k=st;k<arr[i];k++)
			{
				ans=max(ans,prev+k*powi(10,i)+dp[k][len-i]);
			}

			prev+=arr[i]*powi(10,i);
			st=arr[i];
		}

		if(fg)
			ans=max(ans,prev);

		cout<<"Case #"<<test<<": "<<ans<<"\n";
	}
}