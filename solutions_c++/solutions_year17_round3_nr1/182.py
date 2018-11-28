#include <stdio.h>
#include <queue>
#include <algorithm>
#define PHI 3.1415926535897932
void solve();
int main()
{
	freopen("largeA3.in","r",stdin);
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
std::priority_queue<long long int> Q;
void solve()
{
	int a,b;
	double ans = 0;
	scanf("%d%d",&a,&b);
	for(int i=1;i<=a;i++) scanf("%d%d",&x[i].x0,&x[i].y0);
	std::sort(x+1,x+a+1,cmp);
	for(int i=a;i>=b;i--)
	{
		int R = x[i].x0;
		long long int h = (long long int )x[i].y0*x[i].x0;
		for(int j=1;j<i;j++) Q.push((long long int)x[j].x0*x[j].y0);
		for(int j=1;j<b;j++) h+=Q.top(),Q.pop();
		while(!Q.empty()) Q.pop();
		double S = PHI*(double)R*R+2*PHI*h;
		ans = ans>S?ans:S;
	}
	printf("%.12lf\n",ans);
}
