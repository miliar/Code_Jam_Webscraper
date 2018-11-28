#include<cstdio>
#include<algorithm>
#include<cstring>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
int main()
{
	freopen("a.in","r",stdin);freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	int c=0;
	while (T--)
	{
		int d,n;
		scanf("%d%d",&d,&n);
		double ans=1e19;
		fo(i,1,n)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			if (d!=x)
			ans=min(ans,d/((double)(d-x)/y));
		}
		printf("Case #%d: ",++c);
		printf("%lf\n",ans);
	}
}
