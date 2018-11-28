#include<bits/stdc++.h>
using namespace std;
int arr[1000],n,p,ha[4];
int func2()
{
	int ans=ha[0]+(ha[1]+1)/2;
	return ans;
}
// 1 wale 2 wale left 
int dp3[102][102][3];
int dpfunc3(int ek,int two,int lef)
{
	if(ek+two==0)
	return 0;
	int &ans=dp3[ek][two][lef];
	if(ans!=-1)
	return ans;
	ans=0;
	if(ek>0)
	{
		ans+=dpfunc3(ek-1,two,(lef-1+3)%3);
		if(lef==0)
			ans++;
	}
	if(two>0)
	{
		int	ans2=dpfunc3(ek,two-1,(lef-2+3)%3);
		if(lef==0)
			ans2++;
		ans=max(ans,ans2);
	}
	return ans;
}
int func3()
{
	int ans=ha[0]+dpfunc3(ha[1],ha[2],0);
	return ans;
}
int dp4[102][102][102][4];
int dpfunc4(int ek,int two,int teen,int lef)
{
	if(ek+two+teen==0)
	return 0;
	int &ans=dp4[ek][two][teen][lef];
	if(ans!=-1)
	return ans;
	ans=0;
	if(ek>0)
	{
		ans+=dpfunc4(ek-1,two,teen,(lef-1+4)%4);
		if(lef==0)
			ans++;
	}
	if(two>0)
	{
		int	ans2=dpfunc4(ek,two-1,teen,(lef-2+4)%4);
		if(lef==0)
			ans2++;
		ans=max(ans,ans2);
	}
	if(teen>0)
	{
		int	ans2=dpfunc4(ek,two,teen-1,(lef-3+4)%4);
		if(lef==0)
			ans2++;
		ans=max(ans,ans2);
	}
	return ans;
}
int func4()
{
	int ans=ha[0]+dpfunc4(ha[1],ha[2],ha[3],0);
	return ans;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,u=1;
	cin>>t;
	memset(dp3,-1,sizeof(dp3));
	memset(dp4,-1,sizeof(dp4));
	while(t--)
	{
		int i;
		cin>>n>>p;
		memset(ha,0,sizeof(ha));
		for(i=0;i<n;i++)
		{
			cin>>arr[i];
			ha[arr[i]%p]++;
		}
		int ans;
		if(p==2)
		ans=func2();
		else if(p==3)
		ans=func3();
		else if(p==4)
		ans=func4();
		printf("Case #%d: %d\n",u,ans);
		u++;
	}
	return 0;
}
