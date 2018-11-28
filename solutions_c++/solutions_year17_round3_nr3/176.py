#include <stdio.h>
#include <algorithm>
double wtf[55];
void doe()
{
	int n,k,i,i2;
	double l=0.0,r=1.0000001,have,t,need,res=1;
	scanf("%d %d",&n,&k);
	scanf("%lf",&have);
	for(i=1;i<=n;i++)
		scanf("%lf",&wtf[i]);
	for(t=(l+r)/2;r-l>0.0000001;t=(l+r)/2)
	{
		need=0;
		for(i=1;i<=n;i++)
			if(wtf[i]<t)
				need+=t-wtf[i];
		if(need>have)
			r=t;
		else
			l=t;
	}
	for(i=1;i<=n;i++)
	{
		if(wtf[i]>l)
			res*=wtf[i];
		else
			res*=t;
	}
	printf("%lf\n",res);
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