#include <algorithm>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <list>
#include <vector>

using namespace std;

using value_t = double;

value_t solve(unsigned N, unsigned K, value_t U, std::vector<value_t> P)
{
	std::sort(P.rbegin(), P.rend());

	assert(K == N);
	assert(P.size() == N);

	//P.resize(K);

	auto ksum = std::accumulate(P.begin(), P.end(), (value_t)0.0);
	if ((ksum + U) >= K)
		return 1.0;

	if (U > 0) {
		for (size_t i = 0; i < K; ++i) {
			value_t average = (ksum + U) / (K - i);
			if (average >= P[i]) {
				for (size_t j = i; j < K; ++j) {
					P[j] = average;
				}
				break;
			}
			ksum -= P[i];
		}
	}

	value_t result = 1.0;
	for (size_t i = 0; i < K; ++i) {
		result *= P[i];
	}

	return result;
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

		for (unsigned t = 1; t <= T; ++t) {
			unsigned N, K;

			input >> N >> K;

			value_t U;
			input >> U;

			std::vector<value_t> P;

			for (size_t j = 0; j < N; ++j) {
				value_t pj;

				input >> pj;

				P.push_back(pj);
			}

			auto retval = solve(N, K, U, P);

			std::cout << "Case #" << t << ": " << std::fixed << std::setprecision(6) << retval << std::endl;
		}
	}
	return 0;
}
