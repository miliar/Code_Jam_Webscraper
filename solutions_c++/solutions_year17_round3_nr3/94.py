#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;
#define pi acos(-1.0)
double p[1111];
int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
	int T,k;
	int cas=0;
	scanf("%d",&T);
	while(T--)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		//scanf("%d%d",&n,&k);
		double u;
		scanf("%lf",&u);
		for(int i=1;i<=n;i++)scanf("%lf",&p[i]);
		sort(p+1,p+1+n);
		double sp[111];
		int tk=1;
		sp[1]=p[1];
		for(int i=2;i<=n;i++)
		{
			sp[i]=p[i]+sp[i-1];
			if((sp[i]+u)/i>=p[i])tk=i;
		}
		double ans=1;
		for(int i=1;i<=tk;i++)ans*=min((sp[tk]+u)/tk,1.0);
		for(int i=tk+1;i<=n;i++)ans*=p[i];
		printf("Case #%d: %.10f\n",++cas,ans);
		
	}
}