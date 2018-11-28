#include <iostream>
#include <string>

int main(int argc, char** argv) {
	int T;
	std::cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		std::cout << "Case #" << tc << ": ";
		std::string S;
		std::cin >> S;
		int Sl = (int)S.length();
		int K;
		std::cin >> K;

		int result = 0;

		for (int i = 0; i <= Sl - K; i++) {
			if (S[i] == '-') {
				result++;
				for (int j = 0; j < K; j++) {
					S[i + j] = S[i + j] == '-' ? '+' : '-';
				}
			}
		}

		bool check = true;
		for (int i = Sl - K + 1; i < Sl; i++) {
			if (S[i] == '-') {
				check = false;
				break;
			}
		}

		if (check) {
			std::cout << result;
		}
		else {
			std::cout << "IMPOSSIBLE";
		}

		std::cout << '\n';
	}

	return 0;
}