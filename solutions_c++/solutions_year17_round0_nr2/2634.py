#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

std::string solve(std::string S)
{
	for (size_t i = S.size() - 1; i > 0; --i) {
		if (S[i - 1] > S[i]) {
			while (S[i-1] == '0') {
				--i;
			}

			S[i - 1] = S[i - 1] - 1;

			for (size_t j = i; S[j] != '9' && j < S.size(); ++j) {
				S[j] = '9';
			}
		}
	}

	if (S[0] == '0')
		S = S.substr(1);

	return S;
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

			input >> S;

			auto retval = solve(S);

			std::cout << "Case #" << i << ": " << retval << std::endl;
		}
	}
	return 0;
}
