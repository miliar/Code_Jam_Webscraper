#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

char buf[25];

int main() {
	int task;
	scanf("%d", &task);
	for (int task_index = 1; task_index <= task; ++ task_index) {
		scanf(" %s", buf);
		int n = strlen(buf);
		for (int i = 0; i < n - 1; ++ i) {
			if (buf[i] > buf[i + 1]) {
				int it = i;
				while (it > 0 && buf[it] == buf[it - 1]) {
					-- it;
				}
				-- buf[it];
				for (int j = it + 1; j < n; ++ j) {
					buf[j] = '9';
				}
				break;
			}
		}
		long long ret = 0;
		for (int i = 0; i < n; ++ i) {
			ret = ret * 10 + buf[i] - '0';
		}
		printf("Case #%d: %lld\n", task_index, ret);
	}
	return 0;
}
