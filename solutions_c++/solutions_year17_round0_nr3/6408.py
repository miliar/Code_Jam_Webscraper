#include <iostream>

int main() {
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; i++) {
		// state: K people to seat, A x N + B x (N-1) intervals
		long long A = 1, B = 0, N, K;
		std::cin >> N >> K;
		while (K > A + B) {
			K -= A + B;
			if (N % 2) {
				A = 2 * A + B;
			} else {
				B = 2 * B + A;
			}
			N = N / 2;
		}
		if (K > A) {
			N -= 1;
		}
		std::cout << "Case #" << i << ": " << N/2 << " " << (N-1)/2 << std::endl;
	}
	return 0;
}