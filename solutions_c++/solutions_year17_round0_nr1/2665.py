#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

long solve(std::string S, int K)
{
	long retval = 0;

	for (size_t i = 0;i <= S.size() - K; ++i) {
		if (S[i] != '+') {
			// Flip:
			++retval;
			S[i] = '+';

			for (int j = 1; j < K; ++j) {
				if (S[i + j] == '-')
					S[i + j] = '+';
				else
					S[i + j] = '-';
			}
		}
	}

	for (size_t i = S.size() - K + 1; i < S.size(); ++i) {
		if (S[i] != '+')
			return -1;
	}

	return retval;
}

int main(int argc, char *argv[])
{
	if (argc < 2) {
		std::cerr << "Need an input file" << std::endl;
	}
	else {
		std::fstream input;
		input.open(argv[1], std::fstream::in);

		if (!input.is_open())
			return -1;

		unsigned T;
		input >> T;

		for (unsigned i = 1; i <= T; ++i) {
			std::string S;
			int k;

			input >> S >> k;

			auto retval = solve(S, k);
			std::cout << "Case #" << i << ": ";
			if (retval >= 0)
				std::cout << retval << std::endl;
			else
				std::cout << "IMPOSSIBLE" << std::endl;
		}
	}
	return 0;
}
