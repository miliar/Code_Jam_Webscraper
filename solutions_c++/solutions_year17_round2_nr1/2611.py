#include <iostream>
#include <queue>
using namespace std;
typedef long long LL;
const int N = 10005;
const LL INF = 0x3f3f3f3f;

#define BUG

int n,m;
double a,b,x;
int main()
{

#ifdef BUG
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
#endif
	int kk;
	scanf("%d",&kk);
	for (int cc=1;cc<=kk;cc++)
	{
		double t=-1;
		scanf("%lf%d",&x,&m);
		for (int j=0;j<m;j++)
		{
			scanf("%lf%lf",&a,&b);
			t=max(t,(x-a)/b);
		}
		printf("Case #%d: %.6f\n",cc,x/t);
	}
	return 0;
}
/*

3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10

*/
