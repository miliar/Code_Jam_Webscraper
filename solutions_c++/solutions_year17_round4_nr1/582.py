#include <bits/stdc++.h>

const int N = 120;

int n;
int p;
int a[N];

void init() {
	std::cin >> n;
	std::cin >> p;
	for (int i = 1; i <= n; i++) {
		scanf("%d", &a[i]);
	}
}

void work() {
	int cnt[5] = {0, 0, 0, 0, 0};
	for (int i = 1; i <= n; i++) {
		cnt[a[i] % p]++;
	}

	std::vector<int> ini;
	for (int i = 0; i < p; i++) {
		ini.push_back(cnt[i]);
	}

	std::map<std::vector<int>, int> f[5];
	f[0][ini] = 0;
	for (int i = 1; i <= n; i++) {
		std::map<std::vector<int>, int> g[5];
		for (int j = 0; j < p; j++) {
			for (std::map<std::vector<int>, int>::iterator it = f[j].begin(); it != f[j].end(); it++) {
				std::vector<int> u = it->first;
				for (int k = 0; k < p; k++) {
					if (u[k] > 0) {
						std::vector<int> v = u;
						v[k]--;
						g[(j + k) % p][v] = std::max(g[(j + k) % p][v], it->second + (j == 0));
					}
				}
			}
		}
		for (int j = 0; j < p; j++) {
			f[j] = g[j];
		}
	}
	int answer = 0;
	for (int j = 0; j < p; j++) {
		for (std::map<std::vector<int>, int>::iterator it = f[j].begin(); it != f[j].end(); it++) {
			answer = std::max(answer, it->second);
		}
	}
	std::cout << answer << std::endl;
}

int main() {
	freopen("a_large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int testCount;
	std::cin >> testCount;
	for (int i = 1; i <= testCount; i++) {
		printf("Case #%d: ", i);
		init();
		work();
	}

	return 0;
}
