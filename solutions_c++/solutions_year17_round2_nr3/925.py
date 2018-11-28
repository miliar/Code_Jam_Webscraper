#include <stdio.h>
#include <algorithm>
long long e[105],dum[105][105];
double sp[105],dis[105][105];
void doe()
{
	long long n,q,i,i2,i3;
	scanf("%lld %lld",&n,&q);
	for(i=1;i<=n;i++)
		scanf("%lld %lf",&e[i],&sp[i]);
	for(i=1;i<=n;i++)
		for(i2=1;i2<=n;i2++)
		{
			scanf("%lld",&dum[i][i2]);
			if(dum[i][i2]==-1)
				dum[i][i2]=1e18;
		}
	for(i3=1;i3<=n;i3++)
		for(i=1;i<=n;i++)
			for(i2=1;i2<=n;i2++)
				dum[i][i2]=std::min(dum[i][i2],dum[i][i3]+dum[i3][i2]);
	for(i=1;i<=n;i++)
	{
		for(i2=1;i2<=n;i2++)
		{
			if(e[i]>=dum[i][i2])
				dis[i][i2]=(double)dum[i][i2]/sp[i];
			else
				dis[i][i2]=1e18;
		}
	}
	for(i3=1;i3<=n;i3++)
		for(i=1;i<=n;i++)
			for(i2=1;i2<=n;i2++)
				dis[i][i2]=std::min(dis[i][i2],dis[i][i3]+dis[i3][i2]);
	for(i=1;i<=q;i++)
	{
		scanf("%lld %lld",&i2,&i3);
		printf("%.10lf ",dis[i2][i3]);
	}
	printf("\n");
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