#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <string.h>
#define LL long long
using namespace std;
int T;
int n;
LL d,k;
int s;
int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("A-large (1).out","w",stdout);
	scanf("%d",&T);
	for(int case1=1;case1<=T;case1++)
	{
		scanf("%lld%d",&d,&n);
		//printf("%lld %d\n",d,n);
		double ans=1.79e300;
		for(int i=0;i<n;i++)
		{
			scanf("%lld%d",&k,&s);
			//printf("%lld %d\n",k,s);
			if(ans>d*s*1.0/(d-k))
				ans=d*s*1.0/(d-k);
		}
		printf("Case #%d: %f\n",case1,ans);
	}
	return 0;
}
