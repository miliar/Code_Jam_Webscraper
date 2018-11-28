#include <stdio.h>
#include <algorithm>
#define MAX 1000000001
void solve();
int main()
{
	freopen("largeA2.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
struct str{
	int x0;
	int y0;
}x[1010];
bool cmp(str a, str b)
{
	return a.x0<b.x0;
}
void solve()
{
	int a,b;
	double max = 0;
	scanf("%d%d",&a,&b);
	for(int i=1;i<=b;i++) scanf("%d%d",&x[i].x0,&x[i].y0);
	std::sort(x+1,x+b+1,cmp);
	
	for(int i=b;i>=1;i--)
	{
		double s = (double)(a-x[i].x0)/x[i].y0;
		if(max<s) max = s;
	}
	printf("%.12lf\n",a/max);
}
