#include<bits/stdc++.h>
using namespace std;
int is[2][1500];
//last curr minute lef
int dp[2][2][1500][800];
int func(int las,int curr,int minute,int lef)
{
	if(is[curr][minute]!=0)
		return 10000;
	if(lef<0)
		return 10000;
	if(minute==0)
	{
		if(lef!=(curr^1))
		return 10000;
		return ((las==curr)?0:1);
	}
	int& ans=dp[las][curr][minute][lef];
	if(ans!=-1)
		return ans;
	ans=INT_MAX;
	if(curr==0)
	{	
		if(is[curr][minute-1]==0)
			ans=min(ans,func(las,curr,minute-1,lef-1));
		if(is[curr^1][minute-1]==0)
			ans=min(ans,1+func(las,curr^1,minute-1,lef-1));
	}
	else
	{	
		if(is[curr][minute-1]==0)
			ans=min(ans,func(las,curr,minute-1,lef));
		if(is[curr^1][minute-1]==0)
			ans=min(ans,1+func(las,curr^1,minute-1,lef));
	}
	if(ans<0)
	printf("%d %d %d %d %d\n",las,curr,minute,lef,ans);
	return ans;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,l=1;
	cin>>t;
	while(t--)
	{
		int i,j;
		for(i=0;i<1500;i++)
			is[0][i]=is[1][i]=0;
		memset(dp,-1,sizeof(dp));
		int n,m;
		cin>>n>>m;
		for(i=0;i<n;i++)
		{
			int a,b;
			cin>>a>>b;
			is[0][a]++;
			is[0][b]--;
		}
		
		for(i=0;i<m;i++)
		{
			int a,b;
			cin>>a>>b;
			is[1][a]++;
			is[1][b]--;
		}
		for(i=1;i<1500;i++)
		{
			is[0][i]+=is[0][i-1];
			is[1][i]+=is[1][i-1];
		}
		int ans=INT_MAX;
		ans=min(ans,func(0,0,1439,720));
		ans=min(ans,func(1,1,1439,720));
		printf("Case #%d: %d\n",l,ans);
		l++;
	}
	return 0;
}
