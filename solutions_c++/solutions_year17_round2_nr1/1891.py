#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pll pair < ll, ll >
const double INF = 4411111111.0;

int main()
{
	int T;
	//freopen("A-small-attempt2.in","r",stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d",&T);
	for(int tc = 1; tc <= T; tc++)
	{
		double D, H;
		double ans = 0.0;
		cin >> D >> H;
		//printf("%lf %lf\n",D,H);
		for(int i = 0 ; i < H; i++)
		{
			double pos, speed;
			cin >> pos >> speed;
			//printf("%lf %lf\n",pos, speed);
			ans = max(ans , (D - pos) / speed ); //slowest horse
		}
		ans = D / ans;
		//if(ans == 0.0 ) ans = minm;
		printf("Case #%d: %0.7lf\n",tc, ans);

	}
	return 0;
}