
#include <iostream>
#include <iomanip>
#include <algorithm>

void distr(double amount, double *arr, int cnt) {
	for (int i = 0; i < cnt; i++) {
		arr[i] += amount / (double) cnt;
	}
}

void debug(double train, double *prob, int N) {
	/*
	std::cout << std::endl << "debug: " << train << " ";
	for (int i = 0; i < N; i++) {
		std::cout << prob[i] << " ";
	}
	std::cout << std::endl;
	*/
}

int main() {
	int T;

	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, K;
		std::cin >> N >> K;

		double train;
		double prob[N];
		std::cin >> train;
		for (int i = 0; i < N; i++) std::cin >> prob[i];
		std::sort(prob, prob + N);

		int upd = 0;
		while (train > 0) {
			if (upd == N - 1) {
				distr(train, prob, N);
				train = 0;
				debug(train, prob, N);
			} else {
				double amount = (prob[upd+1] - prob[upd]) * (upd + 1);
				if (amount > train) {
					distr(train, prob, upd + 1);
					train = 0;
					debug(train, prob, N);
				} else {
					distr(amount, prob, upd + 1);
					train -= amount;
					upd++;
					debug(train, prob, N);
				}
			}
		}

		double p = 1;
		for (int i = 0; i < N; i++) {
			p *= prob[i];
		}

		std::cout << "Case #" << t << ": " << std::fixed << std::setprecision(7) << p << std::endl;
	}


	return 0;
}
