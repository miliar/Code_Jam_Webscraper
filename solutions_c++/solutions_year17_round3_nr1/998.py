#include <bits/stdc++.h>

const double PI = 3.14159265358979323846;

const int maxn = 1004;

int n = 0;
int k = 0;
std::pair<double, double> cakes[maxn];
double cache[maxn][maxn];

void init () {
	for (int i = 0 ; i <= n ; i++) {
		for (int j = 0 ; j <= n ; j++) {
			cache[i][j] = -1;
		}
	}
}

double f(int n, int k) {
	if (k == 0) {
		return 0;
	}

	if (n < 0) {
		return 0;
	}

	if (cache[n][k] != -1) {
		return cache[n][k];
	}

	// std::cerr << n << " " << k << '\n';

	double ca = PI * cakes[n].first * cakes[n].first + 2 * PI * cakes[n].first * cakes[n].second;

	double ans = ca;

	if (k > 1) {
		for (int j = n - 1 ; j >= 0 ; j--) {
			ans = std::max(ans, ca - PI * cakes[j].first * cakes[j].first + f(j, k - 1));
		}
	}

	return cache[n][k] = ans;
}

void solution () {
	std::cin >> n >> k;

	init();

	for (int i = 0 ; i < n ; i++) {
		double r = 0, h = 0;
		std::cin >> r >> h;
		cakes[i] = {r, h};
	}

	std::sort(cakes, cakes + n);

	auto ans = f(n - 1, k);
	for (int i = n - 2 ; i >= 0 ; i--) {
		ans = std::max(ans, f(i, k));
	}

	printf("%.9lf\n", ans);
}

int main () {
	// std::ios_base::sync_with_stdio(false);

	// std::freopen("x.in", "r", stdin);
	// std::freopen("A-small-attempt0.in", "r", stdin);
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
