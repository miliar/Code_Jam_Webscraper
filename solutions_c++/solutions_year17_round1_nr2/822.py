#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>

const int MAXN = 51;

std::vector<std::pair<int, int> > package[MAXN];
int ptr[MAXN];

int main() {
	int task;
	scanf("%d", &task);
	for (int task_index = 1; task_index <= task; ++ task_index) {
		int n, p;
		scanf("%d %d", &n, &p);
		std::vector<int> per_serve;
		for (int i = 0; i < n; ++ i) {
			int x;
			scanf("%d", &x);
			per_serve.push_back(x);
		}
		for (int i = 0; i < n; ++ i) {
			package[i].clear();
			for (int j = 0; j < p; ++ j) {
				int x;
				scanf("%d", &x);
				int l = (10 * x + 11 * per_serve[i] - 1) / (11 * per_serve[i]);
				int u = 10 * x / (9 * per_serve[i]);
				package[i].push_back(std::make_pair(l, u));
			}
			std::sort(package[i].begin(), package[i].end());
		}
		int ret = 0, serve = 1;
		for (int i = 0; i < n; ++ i) {
			ptr[i] = 0;
		}

		while (true) {
			bool valid = true, success = true;
			for (int i = 0; i < n; ++ i) {
				while (ptr[i] < p && serve > package[i][ptr[i]].second) {
					++ ptr[i];
				}
				if (ptr[i] >= p) {
					valid = false;
					break;
				}
				if (serve < package[i][ptr[i]].first) {
					serve = package[i][ptr[i]].first;
					success = false;
					break;
				}
			}
			if (!valid) {
				break;
			}
			if (success) {
				++ ret;
				for (int i = 0; i < n; ++ i) {
					++ ptr[i];
				}
			}
		}

		printf("Case #%d: %d\n", task_index, ret);
	}
	return 0;
}

