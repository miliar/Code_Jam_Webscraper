#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

int main() {

	int t;

	std::cin >> t;

	for (auto c = 1; c <= t; c++) {
		int d, n;

		std::cin >> d >> n;

		double maxTime = 0.0;

		for (auto i = 0; i < n; i++) {
			int k, s;
			std::cin >> k >> s;
			maxTime = std::max(maxTime, std::max(0, d - k) / double(s));
		}

		double ret = d / maxTime;

		std::cout << "Case #" << c << ": " << std::fixed << std::setprecision(6) << ret << "\n";
	}

	//getchar();
	return 0;

}