#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define REP(i,j,k)  for(int i=(j);i<=(k);++i)
#define REPD(i,j,k) for(int i=(j);i>=(k);--i)


void init()
{
	double D,mx=0;
	int n;
	scanf("%lf%d",&D,&n);

	while(n--)
	{
		double x,y;
		scanf("%lf%lf",&x,&y);
		mx=max(mx,(D-x)/y);
	}
	printf("%.10lf\n",D/mx);
}

void solve()
{
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	REP(i,1,T)
	{
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
