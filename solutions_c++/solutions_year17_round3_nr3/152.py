#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>

int main() {
	int task;
	scanf("%d", &task);
	for (int task_id = 1; task_id <= task; ++ task_id) {
		int n, k;
		scanf("%d %d", &n, &k);
		double u;
		scanf("%lf", &u);
		std::vector<double> p;
		for (int i = 0; i < n; ++ i) {
			double tmp;
			scanf("%lf", &tmp);
			p.push_back(tmp);
		}
		sort(p.begin(), p.end());
		p.push_back(1.1);
		double rem = u;
		for (int i = 1; i <= n; ++ i) {
			if ((p[i] - p[i - 1]) * i > rem) {
				double last = p[i - 1] + rem / i;
				for (int j = 0; j < i; ++ j) {
					p[j] = last;
				}
				break;
			}
			else {
				rem -= (p[i] - p[i - 1]) * i;
			}
		}
		double ret = 1.0;
		for (int i = 0; i < n; ++ i) {
			ret *= p[i];
		}
		printf("Case #%d: %.6f\n", task_id, ret);
	}
}

