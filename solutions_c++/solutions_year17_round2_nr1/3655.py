#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <tuple>

using namespace std;

int main()
{
	int T, N;
	double D, pos, v, ans;

	freopen("A-large.in", "r", stdin);
	freopen("output-A-large.txt", "w", stdout);

	scanf("%d", &T);

	for(int test_case=1;test_case<=T;test_case++)
	{
		scanf("%lf %d", &D, &N);
		
		ans = 1e18;
		for(int i=1;i<=N;i++)
		{
			scanf("%lf %lf", &pos, &v);

			ans = min(ans, v*D/(D-pos));
		}

		printf("Case #%d: %.9lf\n", test_case, ans);
	}

	return 0;
}