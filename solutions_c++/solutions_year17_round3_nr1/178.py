#include <stdio.h>
double M_PI=3.1415926535897932384626433832;
#include <algorithm>
struct x
{
	double rad,h;
}arr[1005];
bool operator<(x a,x b)
{
	return a.rad>b.rad;
}
void doe()
{
	int n,k,i,i2;
	double maxx=0,now=0,sum,kid[1005];
	scanf("%d %d",&n,&k);
	for(i=1;i<=n;i++)
		scanf("%lf %lf",&arr[i].rad,&arr[i].h);
	std::sort(arr+1,arr+1+n);
	for(i=1;i+k-1<=n;i++)
	{
		//printf("%d\n",i);
		now=M_PI*arr[i].rad*arr[i].rad;
		now+=2*M_PI*arr[i].rad*arr[i].h;
		for(i2=1;i+i2<=n;i2++)
			kid[i2]=2*M_PI*arr[i+i2].rad*arr[i+i2].h;
		std::sort(kid+1,kid+1+n-i);
		for(i2=1;i2<k;i2++)
			now+=kid[n-i-i2+1];
		maxx=std::max(maxx,now);
	}
	printf("%lf\n",maxx);
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