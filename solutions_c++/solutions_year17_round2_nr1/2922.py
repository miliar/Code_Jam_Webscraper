#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;

int main()
{
	int tests, test = 1;
	int k, d, n, s;
	double ans, maxTime;

	scanf("%d", &tests);
	while(tests--) {
		scanf(" %d %d", &d, &n);
		maxTime = 0.0;
		for (int i = 0; i < n; ++i)
		{
			scanf(" %d %d", &k, &s);
			maxTime = max(maxTime, (double)(d - k) / (double)(s));
		}
		ans = (double)(d) / maxTime;

		printf("Case #%d: %.10f\n", test++, ans);
	}
	
	return 0;
}