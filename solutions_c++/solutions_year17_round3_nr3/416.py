#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN=1500;
const int oo=1000000000;

double p[MAXN],u,ans;
int i,j,k,n,m;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int DAT;
	scanf("%d",&DAT);
	for (int cas=1;cas<=DAT;cas++)
	{
		ans=1;
		scanf("%d%d",&n,&m);
		scanf("%lf",&u);
		for (i=1;i<=n;i++)
			scanf("%lf",p+i);
		sort(p+1,p+n+1);
		p[n+1]=1;
		for (i=1;i<=n;i++)
			if (u>=(p[i+1]-p[i])*i)
			{
				u-=(p[i+1]-p[i])*i;
				for (j=1;j<=i;j++)
					p[j]=p[i+1];
			}
			else
			{
				for (j=1;j<=i;j++)
					p[j]+=u/i;
				break;
			}
		for (i=1;i<=n;i++) ans*=p[i];
		printf("Case #%d: %lf\n",cas, ans);
	}
	return 0;
}