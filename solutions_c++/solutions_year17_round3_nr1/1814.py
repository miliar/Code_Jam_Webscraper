#include<bits/stdc++.h>
using namespace std;

int n,k;
double pi=3.14159265358979;
		  
vector<pair<long long int,long long int> > m;
vector<vector<long long int> > dp;

long long int func(int index,int cnt)
{
	if(cnt+index+1<k)
	{//printf("lol\n");
		return -100000000000000007;
	}
	if(index==-1)
	{
		if(cnt==k)
		{
			return 0;
		}
		else
		{
			return -100000000000000007;
		}
	}
	long long int ans,ans1,ans2;

	if(dp[index][cnt]!=-1)
	{//printf("rec\n");
		return dp[index][cnt];
	}

		ans1=func(index-1,cnt);
		ans2=2*(m[index].first)*(m[index].second);
		ans2+=func(index-1,cnt+1);

	ans=max(ans1,ans2);
	dp[index][cnt]=ans;
	
	return ans;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int it=1;it<=t;it++)
	{
		scanf("%d %d",&n,&k);
		m.clear();
		m.resize(n);
		for(int i=0;i<n;i++)
		{
			scanf("%lld %lld",&(m[i].first),&(m[i].second));
		}
		sort(m.begin(), m.end());
		dp.clear();
		dp.resize(n+2,vector<long long int>(n+2,-1));
		long long int ans=-100000000000000007;
		for(int i=n-1;i>=k-1;i--)
		{
			ans=max(ans,(m[i].first*m[i].first)+2*(m[i].first)*(m[i].second)+func(i-1,1));
		}
		double final;
		final=ans*pi;
		printf("Case #%d: %0.9lf\n",it,final );
	}
	return 0;
}