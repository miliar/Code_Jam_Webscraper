#include <iostream>

int main()
{
	int T;
	std::cin >> T;

	for (int i = 0; i < T; ++i) {
		std::string S;
		unsigned int K;
		std::cin >> S >> K;

		std::cerr << "S = " << S << ", K = " << K << '\n';

		int n = 0;

		while (true) {
			// first '-'
			auto pos = S.find('-');
			std::cerr << "pos = " << pos << '\n';

			if (pos == std::string::npos)
				break;

			if (S.size() - pos < K) {
				n = -1;
				break;
			}

			// flip from first '-' pos
			for (auto j = pos; j < pos + K; ++j) {
				S[j] = (S[j] == '-') ? '+' :  '-';
			}

			std::cerr << "S = " << S << '\n';

			++n;
		}

		std::cout << "Case #" << i + 1 << ": ";
		if (n >= 0)
			std::cout << n << '\n';
		else
			std::cout << "IMPOSSIBLE\n";
	}

	return 0;
}
