#include <bits/stdc++.h>

#define INF 1000000000000000;

const int maxn = 10000;

double d = 0;
int n = 0;

double a[maxn];
double v[maxn];

void init () {}

void solution () {
	std::cin >> d >> n;
	// std::cerr << n << '\n';
	for (int i = 0 ; i < n ; i++) {
		std::cin >> a[i] >> v[i];
	}

	// init();

	double ans = (d * v[0]) / (d - a[0]);
	// std::cerr << ans << '\n';

	for (int i = 1 ; i < n ; i++) {
		auto cans = (d * v[i]) / (d - a[i]);
		// std::cerr << cans << '\n';
		ans = std::min(ans, cans);
	}

	printf("%.6lf\n", ans);
}

int main () {
	// std::ios_base::sync_with_stdio(false);

	// std::freopen("x.in", "r", stdin);
	// std::freopen("A-small-attempt0.in", "r", stdin);
	// std::freopen("A-small-attempt1.in", "r", stdin);
	std::freopen("A-large.in", "r", stdin);

	std::freopen("A.out", "w", stdout);

	int T = 0;
	std::cin >> T;
	std::cin.ignore(10000, '\n');
	for (int i = 1 ; i <= T ; i += 1) {
		std::cerr << "Case #" << i << "\n";
		std::cout << "Case #" << i << ": ";
		solution();
	}

	return 0;
}
