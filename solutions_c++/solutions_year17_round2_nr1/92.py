#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

const int maxn=1010;

int n;

double D,k[maxn],s[maxn];

int main()
{
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%lf%d",&D,&n);
		for (int a=1;a<=n;a++)
			scanf("%lf%lf",&k[a],&s[a]);
		double ans=1e+20;
		for (int a=1;a<=n;a++)
			ans=min(ans,D/((D-k[a])/s[a]));
		printf("Case #%d: %.6lf\n",t,ans);
	}

	return 0;
}
