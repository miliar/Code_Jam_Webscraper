#include <cstdio>

using namespace std;

int T;

int main()
{
	scanf("%d",&T);
	for (int t = 1; t <= T; t ++)
	{
		int d,n;
		scanf("%d%d",&d,&n);
		double maxtime = 0.0;
		for (int i = 1; i <= n; i ++)
		{
			int k,s;
			scanf("%d%d",&k,&s);
			double temp = (double)(d - k) / s;
			if (temp > maxtime)
				maxtime = temp;
		}
		double ans = d / maxtime;
		printf("Case #%d: %.6f\n",t,ans);

	}
	return 0;
}