#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn)
	{
		int D, N;
		scanf("%d%d", &D, &N);
		double last_time = 0;
		for (int i = 0; i < N; ++i)
		{
			int K, S;
			scanf("%d%d", &K, &S);
			double cur = (D - K) * 1.0 / S;
			last_time = max(last_time, cur);
		}
		printf("Case #%d: %.10lf\n", cn, D * 1.0 / last_time);
	}
}