#include<bits/stdc++.h>
using namespace std;

long long dp[20][15][2];
long long num;

int dig;

void init(long long k)
{
	num=k;
}

int getdig(int pos)
{
	long long x=pow(10,dig-pos);
	long long p=num/x;
//	cout<<"fun "<<num<<"  "<<x<<" ";
	return p%10;
}

int finddig(long long p)
{
	int cnt=0;
	long long x=p;
	while(x)
	{
		x/=10;
		cnt++;
	}
	
	return cnt;
}

long long solve(int pos,int last,int ok)
{

	if(pos>dig)
	return 1;
	
	if(dp[pos][last][ok]!=-1)
	return dp[pos][last][ok];
	
	int i;
	
	long long ans=0;
	
	for (i=last;i<=9;i++)
	{
		if(ok)
		{
			int p=getdig(pos);
	
			if(p<i)
			break;
			
			if(p==i)
			ans+=solve(pos+1,i,1);
			
			else
			ans+=solve(pos+1,i,0);
		}
		
		else
		{
			ans+=solve(pos+1,i,0);
		}
		
	}
	
	
	return dp[pos][last][ok]=ans;
}





int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	
	for (int t=1;t<=T;t++)
	{
		long long N,num;
		scanf("%lld",&N);
		init(N);

	
		memset(dp,-1,sizeof(dp));
		dig=finddig(N);

		long long p=solve(1,0,1);
	
		long long l=1,r=N,best=r;
		
		while(l<=r)
		{
			long long mid=(l+r)/2;
			init(mid);
			dig=finddig(mid);
			
			memset(dp,-1,sizeof(dp));
			if(solve(1,0,1)==p)
			{
				best=min(best,mid);
				r=mid-1;
			}
			
			else
			l=mid+1;
			
		}
		
		printf("Case #%d: %lld\n",t,best);
	}
}
