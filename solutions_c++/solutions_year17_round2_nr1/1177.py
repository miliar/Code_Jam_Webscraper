
#include <iostream>
#include <iomanip>

int main() {

	int T;
	std::cin >> T;

	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";

		int D, N;
		std::cin >> D >> N;

		double slowest = -1;
		for (int n = 0; n < N; n++) {
			int K, S;
			std::cin >> K >> S;

			double time = (double) (D-K) / (double) S;
			if (slowest < 0) {
				slowest = time;
			} else {
				if (time > slowest) {
					slowest = time;
				}
			}
		}

		std::cout << std::fixed << std::setprecision(7) << ((double) D / slowest) << std::endl;
	}

	return 0;

}

