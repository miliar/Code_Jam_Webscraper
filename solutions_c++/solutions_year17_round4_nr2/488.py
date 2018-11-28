#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#include <numeric>

const int MAXC = 1111;

int cnt[MAXC], ticket[MAXC], sum[MAXC];

int main() {
	int task;
	scanf("%d", &task);
	for (int task_id = 1; task_id <= task; ++ task_id) {
		int n, c, m;
		scanf("%d %d %d", &n, &c, &m);
		for (int i = 0; i <= c; ++ i) {
			cnt[i] = 0;
		}
		for (int i = 0; i <= n; ++ i) {
			ticket[i] = 0;
			sum[i] = 0;
		}
		int ret = 0, way = 0;
		for (int i = 0; i < m; ++ i) {
			int x, y;
			scanf("%d %d", &x, &y);
			ret = std::max(ret, ++ cnt[y]);
			++ ticket[x];
		}
		for (int i = 1; i <= n; ++ i) {
			sum[i] = sum[i - 1] + ticket[i];
			int z = sum[i] / i + (sum[i] % i > 0 ? 1 : 0);
			ret = std::max(ret, z);
		}
		for (int i = 0; i <= n; ++ i) {
			if (ret < ticket[i]) {
				way += ticket[i] - ret;
			}
		}
		printf("Case #%d: %d %d\n", task_id, ret, way);
	}
	return 0;
}

