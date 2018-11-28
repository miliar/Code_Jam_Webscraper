#include<bits/stdc++.h>
using namespace std;
int arr[20],p;
//0 means equal 1 means less
//length isless last
long long int dp[20][2][10];
long long int func(int in,int isless,int last)
{
	if(in==-1)
		return 1;
	long long int &ans=dp[in][isless][last];
	if(ans!=-1)
	return ans;
	ans=0;
	if(isless==1)
	{
		for(int i=last;i<10;i++)
			ans=(ans+func(in-1,isless,i));
		return ans;
	}
	for(int i=last;i<=arr[in];i++)
		ans=(ans+func(in-1,(i==arr[in])?0:1,i));
	return ans;
}
long long int fun(long long int n)
{
		memset(dp,-1,sizeof(dp));
		long long int temp=n;
		p=0;
		while(temp)
		{
			arr[p++]=temp%10;
			temp/=10;
		}
		long long int ans=func(p-1,0,0);
		return ans;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,l;
	cin>>t;
	for(l=1;l<=t;l++)
	{
		long long int n;
		cin>>n;
		long long int pre=fun(n);
		long long int low=1,high=n;
		while(low<high)
		{
			long long int mid=(low+high)/2;
			if(fun(mid)==pre)
				high=mid;
			else
				low=mid+1;
		}
		printf("Case #%d: ",l);
		printf("%lld\n",low);
	}
	return 0;
}
