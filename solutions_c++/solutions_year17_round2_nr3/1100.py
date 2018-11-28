
#include <iostream>
#include <iomanip>

int main() {

	int T;
	std::cin >> T;

	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";

		int N, Q;
		std::cin >> N >> Q;

		int E[N], S[N];
		for (int i = 0; i < N; i++) {
			std::cin >> E[i] >> S[i];
		}

		int D[N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int d;
				std::cin >> d;
				if (j == i+1) D[i] = d;
			}
		}
		int U, V;
		std::cin >> U >> V;

		double time[N];
		time[N-1] = 0;
		time[N-2] = (double) D[N-2] / (double) S[N-2];

		for (int x = N-3; x >= 0; x--) {
			time[x] = -1;
			int dtot = D[x];
			for (int y = x+1; y < N && dtot <= E[x]; y++) {
				
				double t = (double) dtot / (double) S[x] + time[y];
				if (time[x] < 0 || time[x] > t) time[x] = t;

				dtot += D[y];
			}
		}

		std::cout << std::fixed << std::setprecision(7) << time[0] << std::endl;
	}

	return 0;

}

