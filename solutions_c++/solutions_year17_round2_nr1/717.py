#include <bits/stdc++.h>
#define ii pair<int, int>
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define vii vector< pair<int, int> >
typedef long long ll;
using namespace std;
double x[1005], v[1005];
int main()
{
    int tt;
    scanf("%d", &tt);
    for(int qq = 1; qq<= tt; qq++)
    {
        double clock_start = clock();
		double d;
		int n;
		scanf("%lf %d", &d, &n);
		for(int i = 1; i<= n; i++)
		{
			scanf("%lf %lf", x+i, v+i);
		}
		double ans = 1e18;
		for(int i = 1; i<= n; i++)
		{
			for(int j = 1; j<= n; j++)
			{
				if(i == j) continue;
				double x1 = x[i], x2 = x[j];
				double v1 = v[i], v2 = v[j];
				if(v1 == v2) continue;
				double elap = (x2-x1)/(v1-v2);
				if(elap< 0) continue;
				double meet = x2+v2*elap;
				if(meet> d) continue;
				double more = (d-meet)/v2;
				ans = min(ans, d/(more+elap));
			}
		}
		for(int i = 1; i<= n; i++)
		{
			double more = (d-x[i])/v[i];
			ans = min(ans, d/more);
		}
        printf("Case #%d: ", qq);
		printf("%lf\n", ans);
        fprintf(stderr, "Test %d solved in %.2lf s.\n", qq, (clock()-clock_start)/CLOCKS_PER_SEC);
    }
	return 0;
}
