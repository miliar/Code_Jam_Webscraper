#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

double const eps = 0.0000000000001;

bool possible(std::vector<double> &P, double U, double min_p) {
	for (double p : P)
		if (p < min_p)
			U -= (min_p - p);
	return U >= 0;
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cout << std::setprecision(10);
	int T, N, K;
	double U;
	std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		std::cin >> N >> K;
		std::cin >> U;
		std::vector<double> P(N, 0.0);
		for (int i = 0; i < N; ++i)
			std::cin >> P[i];
		double b = 0.0, e = 1.0, mid;
		while (std::abs(b - e) > eps) {
			mid = (b + e) / 2;
			if (possible(P, U, mid)) b = mid;
			else e = mid;
		}
		double ans = 1.0;
		for (double p : P) {
			if (p < mid) ans *= mid;
			else ans *= p;
		}
		std::cout << "Case #" << t << ": " << ans << std::endl;
	}
	return 0;
}
