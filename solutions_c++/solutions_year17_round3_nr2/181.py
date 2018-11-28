#include <stdio.h>
#include <algorithm>
int stat[1440],dp[1450][730][2][2];
int wtf(int min,int la,int last,int fix)
{
	//printf("%d %d %d\n",min,la,last);
	int lb=min-la,a,b;
	if(la>720||lb>720)
		return 999999;
	if(min==1440)
		return 0;
	if(dp[min][la][last][fix]!=-1)
		return dp[min][la][last][fix];
	if(stat[min]==0)
	{
		if(last==0)
		{
			a=wtf(min+1,la+1,0,fix);
			b=1+wtf(min+1,la,1,fix);
		}
		else
		{
			a=1+wtf(min+1,la+1,0,fix);
			b=wtf(min+1,la,1,fix);
		}
		if(min==1439)
		{
			if(fix==0)
				dp[min][la][last][fix]=a;
			else
				dp[min][la][last][fix]=b;
		}
		else
			dp[min][la][last][fix]=std::min(a,b);
		//printf("%d %d\n",dp[min][la][last]);
	}
	else if(stat[min]==1)
	{
		if(min==1439&&fix==0)
			return 999999;
		if(last==1)
			dp[min][la][last][fix]=wtf(min+1,la,1,fix);
		else
			dp[min][la][last][fix]=1+wtf(min+1,la,1,fix);
		//printf("%d\n",dp[min][la][last]);
	}
	else
	{
		if(min==1439&&fix==1)
			return 999999;
		if(last==0)
			dp[min][la][last][fix]=wtf(min+1,la+1,0,fix);
		else
			dp[min][la][last][fix]=1+wtf(min+1,la+1,0,fix);
		//printf("%d\n",dp[min][la][last]);
	}
	//printf("%d %d %d %d\n",min,la,last,dp[min][la][last]);
	return dp[min][la][last][fix];
}
void doe()
{
	int n,m,i,i2,t,tt,i3,i4;
	for(i=0;i<1440;i++)
		stat[i]=0;
	for(i=0;i<1450;i++)
		for(i2=0;i2<730;i2++)
			for(i3=0;i3<2;i3++)
				for(i4=0;i4<2;i4++)
					dp[i][i2][i3][i4]=-1;
	scanf("%d %d",&n,&m);
	for(i=1;i<=n;i++)
	{
		scanf("%d %d",&t,&tt);
		for(i2=t;i2<tt;i2++)
			stat[i2]=1;
	}
	for(i=1;i<=m;i++)
	{
		scanf("%d %d",&t,&tt);
		for(i2=t;i2<tt;i2++)
			stat[i2]=2;
	}
	printf("%d\n",std::min(wtf(0,0,0,0),wtf(0,0,1,1)));
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		doe();
	}
	return 0;
}