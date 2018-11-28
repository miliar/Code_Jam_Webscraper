#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
const int maxn = 1005;
int n;
double sum, k[maxn], s[maxn], time;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		int now;
		scanf("%lf%d", &sum, &n);
		time = 0;
		for (int i = 1; i <= n; i++)
		{
			scanf("%lf%lf", &k[i], &s[i]);
			double tmp = (sum - k[i]) / s[i];
			if (tmp > time)
				time = tmp;
		}
		printf("Case #%d: %.6f\n", tt, sum / time);
	}
	return 0;
}
