#include <cstdio>
using namespace std;


int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int d, n;
		scanf("%d %d", &d, &n);
		double lastFinish = 0;
		for (int i = 0; i < n; ++i) {
			int k, s;
			scanf("%d %d", &k, &s);
			double finishTime = (double)(d - k) / (double)s;
			if (finishTime > lastFinish)
				lastFinish = finishTime;
		}
		double maxSpeed = (double)d / lastFinish;
		printf("Case #%d: %.6lf\n", t+1, maxSpeed);
	}
	return 0;
}
