#include <cstdio>

int main() {
	int t;
	scanf("%d", &t);
	for (int _t = 1; _t <= t; _t++) {
		int d, n;
		double time = 0;
		scanf("%d %d", &d, &n);
		for (int i = 0; i < n; i++) {
			double k, s;
			scanf("%lf %lf", &k, &s);
			double time_ = (d-k)/s;
			if (time_ > time)
				time = time_;
		}
		printf ("Case #%d: %lf\n", _t, d/time);
	}
}

