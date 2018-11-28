#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

const int MAXN = 1111;
const double PI = acos(-1.0);

int radius[MAXN], height[MAXN];

long long square(int x) {
	return (long long)x * x;
}

long long area(int r, int h) {
	return (long long)r * h * 2;
}

int main() {
	int task;
	scanf("%d", &task);
	for (int task_id = 1; task_id <= task; ++ task_id) {
		int n, k;
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; ++ i) {
			scanf("%d %d", radius + i, height + i);
		}
		long long ret = 0;
		for (int i = 0; i < n; ++ i) {
			long long sum = square(radius[i]) + area(radius[i], height[i]);
			std::vector<long long> v;
			for (int j = 0; j < n; ++ j) {
				if (i != j) {
					v.push_back(area(radius[j], height[j]));
				}
			}
			std::sort(v.begin(), v.end(), std::greater<long long>());
			for (int j = 0; j < k - 1; ++ j) {
				sum += v[j];
			}
			ret = std::max(ret, sum);
		}
		printf("Case #%d: %.6f\n", task_id, ret * PI);
	}
	return 0;
}

