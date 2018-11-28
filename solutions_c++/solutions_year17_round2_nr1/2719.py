#include <iostream>
#include <string>

void solve() {
	int d, n;
	std::cin >> d >> n;
	long double k, s, m, tmp;
	std::cin >> k >> s;
	m = (d - k)/s;
	for (int i = 1; i < n; ++i) {
		std::cin >> k >> s;
		tmp = (d - k)/s;
		m = m > tmp ? m : tmp;
	}
	std::cout.precision(8);
	std::cout << d/m;
	return;
}

int main() {
	int t;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		std::cout << "Case #" << i + 1 << ": ";
		solve();
		std::cout << std::endl;
	}
	return 0;
}
