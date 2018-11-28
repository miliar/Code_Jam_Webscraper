#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string.h>
using namespace std;

const double pi=acos(-1);

struct c
{
	long long r,h;
};

long long dp[1050];
c cake[1000];

bool yee(c a,c b)
{
	if(a.r==b.r) return a.h>b.h;
	return a.r>b.r;
}

int main()
{
	long long t,n,i,j,x=0,k;
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld%lld",&n,&k);
		for(i=0;i<n;i++) scanf("%lld%lld",&cake[i].r,&cake[i].h);
		sort(cake,cake+n,yee);
		memset(dp,0,sizeof(dp));
		dp[1]=cake[0].r*cake[0].r+2*cake[0].r*cake[0].h;
		for(i=1;i<n;i++)
		{
			for(j=i;j>0;j--)
				if(dp[j+1]<dp[j]+2*cake[i].r*cake[i].h) dp[j+1]=dp[j]+2*cake[i].r*cake[i].h;
			if(dp[1]<cake[i].r*cake[i].r+2*cake[i].r*cake[i].h) dp[1]=cake[i].r*cake[i].r+2*cake[i].r*cake[i].h;
		}
		printf("Case #%lld: %.9lf\n",++x,(double)dp[k]*pi);
	}
}
