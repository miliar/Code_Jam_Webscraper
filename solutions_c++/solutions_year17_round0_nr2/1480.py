
#include <iostream>

typedef unsigned long long ull;

ull tidier(ull x) {
	ull pre = x;
	ull post = 0;
	ull o = 1;
	while (pre > 0) {
		ull spre = pre / 10;
		int d1 = pre % 10;
		int d2 = spre % 10;

		post = d1 * o + post;
		o *= 10;

		if (d2 > d1) {
			return x - post - 1;
		}

		pre = spre;
	}
	return x;
}

int main() {
	int T;
	std::cin >> T;

	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";

		ull N, N1;
		std::cin >> N;
		while ((N1 = tidier(N)) != N) {
			//std::cout << "(" << N1 << " tidier than " << N << ") ";
			N = N1;
		}
		std::cout << N << std::endl;
	}
	return 0;
}
