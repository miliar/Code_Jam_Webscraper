#include <stdio.h>
#include <algorithm>
struct x
{
	double pos,sp;
}arr[1005];
bool operator<(x a,x b)
{
	if(a.pos==b.pos)
		return a.sp>b.sp;
	return a.pos<b.pos;
}
void doe()
{
	int n,i,i2,fuck,minpos;
	double l,r,t,time=0,minn,d;
	scanf("%lf %d",&d,&n);
	for(i=1;i<=n;i++)
		scanf("%lf %lf",&arr[i].pos,&arr[i].sp);
	std::sort(arr+1,arr+1+n);
	while(arr[1].pos<d&&n>1)
	{
		minn=1e18;
		fuck=0;
		for(i=1;i<n;i++)
		{
			if(arr[i].sp>arr[i+1].sp)
			{
				if((arr[i+1].pos-arr[i].pos)/(arr[i].sp-arr[i+1].sp)<minn)
				{
					minn=(arr[i+1].pos-arr[i].pos)/(arr[i].sp-arr[i+1].sp);
					minpos=i;
				}
				fuck=1;
			}
		}
		if(fuck==0)
			break;
		for(i=1;i<=n;i++)
			arr[i].pos+=minn*arr[i].sp;
		if(arr[1].pos>d)
		{
			arr[1].pos-=arr[1].sp*minn;
			break;
		}
		for(i=minpos;i<n;i++)
			arr[i]=arr[i+1];
		time+=minn;
		n--;
	}
	if(arr[1].pos<d)
	{
		time+=(d-arr[1].pos)/arr[1].sp;
	}
	printf("%.10lf\n",d/time);
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