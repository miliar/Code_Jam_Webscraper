#include <bits/stdc++.h>


const int maxn = 55;

int n = 0, k = 0;
double u;
double p[maxn];
double s;

void init () {
	s = 0;
}

void print() {
	for (int i = 0 ; i < n ; i++) {
		std::cerr << p[i] << ' ';
	}
	std::cerr << '\n';
}

void solution () {
	std::cin >> n >> k;

	init();

	std::cin >> u;
	for (int i = 0 ; i < n ; i++) {
		std::cin >> p[i];
		s += p[i];
	}

	std::sort(p, p + n);

	for (int i = 0 ; i < n - 1 && u > 0 ; i++) {
		auto d = p[i + 1] - p[i];
		auto need = (i + 1) * d;
		if (u >= need) {
			u -= need;
			for (int j = 0 ; j <= i ; j++) {
				p[j] = p[i + 1];
			}
		} else {
			auto av = u / (i + 1);
			for (int j = 0 ; j <= i ; j++) {
				p[j] += av;
			}
			u -= av * (i + 1);
		}
		// print();
	}

	if (u > 0) {
		auto av = u / n;
		for (int i = 0 ; i < n ; i++) {
			p[i] += av;
		}
	}

	double ans = 1;

	for (int i = 0 ; i < n ; i++) {
		ans *= p[i];
	}

	printf("%.9lf\n", ans);
}

int main () {
	// std::ios_base::sync_with_stdio(false);

	// std::freopen("x.in", "r", stdin);
	// std::freopen("C-small-1-attempt0.in", "r", stdin);
	// std::freopen("C-small-1-attempt1.in", "r", stdin);
	std::freopen("C-small-1-attempt2.in", "r", stdin);
	// std::freopen("C-large.in", "r", stdin);

	std::freopen("C.out", "w", stdout);

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
