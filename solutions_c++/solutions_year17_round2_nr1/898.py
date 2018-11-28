#include <cstdio>
#include <algorithm>
using namespace std;


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1l.out","w",stdout);
	int t;
	int ca = 0;
	scanf("%d",&t);
	int n,d;
	while(t--)
	{
		scanf("%d%d",&d,&n);
		long long k,s;
		double Min = 0;
		for(int i = 1; i <= n; ++i)
		{
			scanf("%lld%lld",&k,&s);
			Min = max(Min,(d-k)*1.0/s);
		}
		printf("Case #%d: %.6f\n",++ca,d/Min);
	}


	return 0;
}


