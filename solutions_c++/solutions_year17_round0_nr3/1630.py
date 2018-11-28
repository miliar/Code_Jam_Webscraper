#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

int main() {
	int task;
	scanf("%d", &task);
	for (int task_index = 1; task_index <= task; ++ task_index) {
		long long n, k;
		scanf("%lld %lld", &n, &k);
		long long ret = n;
		if (k > 1) {
			long long p = 1;
			while ((k - 2) >> 1 >= p) {
				p = (p << 1) + 1;
			}
			long long r = k - p;
			long long a = n - p, b = p + 1;
			ret = r <= a % b ? a / b + 1 : a / b;
		}
		printf("Case #%d: %lld %lld\n", task_index, ret >> 1, (ret - 1) >> 1);
	}
	return 0;
}

