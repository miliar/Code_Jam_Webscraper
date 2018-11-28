#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;
#define pi acos(-1.0)
struct node
{
	long long r,h;
	node(){}
	node(long long r,long long h):r(r),h(h){}
	bool operator<(const node &b)const
	{
		if(r*h!=b.r*b.h)
		return r*h>b.r*b.h;
		return r>b.r;
	}	
}e[1111];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,k;
	int cas=0;
	scanf("%d",&T);
	while(T--)
	{
		cas++;
		int n;
		scanf("%d%d",&n,&k);
		for(int i=1;i<=n;i++)scanf("%lld%lld",&e[i].r,&e[i].h);
		sort(e+1,e+1+n);
		long long sum=0;
		long long maxr2=e[1].r*e[1].r;
		for(int i=1;i<k;i++)
		{
			if(e[i].r*e[i].r>maxr2)maxr2=e[i].r*e[i].r;
			sum+=e[i].r*e[i].h*2;
		}
		long long ans=0;
		for(int i=k;i<=n;i++)
		{
			ans=max(ans,sum+e[i].r*e[i].h*2+max(maxr2,e[i].r*e[i].r));
		}
		printf("Case #%d: %.10f\n",cas,pi*ans);
	}
}