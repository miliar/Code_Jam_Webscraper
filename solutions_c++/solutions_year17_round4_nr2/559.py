#include <bits/stdc++.h>

const int N = 1e3 + 100;

int n, m;
int c;
std::pair<int, int> ticket[N];

void init() {
	std::cin >> n >> c >> m;
	for (int i = 1; i <= m; i++) {
		scanf("%d%d", &ticket[i].first, &ticket[i].second);
	}
}

void work() {
	static int cnt[N];
	static int a[N];
	std::memset(cnt, 0, sizeof(cnt));
	std::memset(a, 0, sizeof(a));

	for (int i = 1; i <= m; i++) {
		cnt[ticket[i].second]++;
		a[ticket[i].first]++;
	}
	std::pair<int, int> answer = std::make_pair(0, 0);
	for (int i = 1; i <= c; i++) {
		answer.first = std::max(answer.first, cnt[i]);
	}
	for (int i = 1; i <= n; i++) {
		a[i] += a[i - 1];
		answer.first = std::max(answer.first, (a[i] + i - 1) / i);
	}
	for (int i = 1; i <= n; i++) {
		answer.second += std::max(0, a[i] - a[i - 1] - answer.first);
	}
	std::cout << answer.first << " " << answer.second << std::endl;
}

int main() {
	freopen("b_large.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int testCount;
	std::cin >> testCount;
	for (int i = 1; i <= testCount; i++) {
		printf("Case #%d: ", i);
		init();
		work();
	}

	return 0;
}
