#include <iostream>
#include <iomanip>

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cout << std::setprecision(10);
	int T, N;
	std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		double D, K, S, time = 0;
		std::cin >> D >> N;
		while (N--) {
			std::cin >> K >> S;
			time = std::max((D - K) / S, time);
		}
		std::cout << "Case #" << t << ": " << D / time << std::endl;
	}
	return 0;
}
