#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

using value_t = uint64_t;

std::pair<value_t, value_t> solve(value_t N, value_t K)
{
	std::map<value_t, value_t> spaces;
	spaces[N] = 1;

	while (K > 0 && !spaces.empty()) {
		auto last = *spaces.rbegin();

		auto space = last.first;
		auto count = last.second;

		if (K <= count) {
			return { space/2, (space - 1)/2};
		}

		K-= count;

		spaces[(space -1)/2] = spaces[(space -1)/2] + count;
		spaces[space/2] = spaces[space/2] + count;

		spaces.erase(space);
	}

	return {0, 0};
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
			value_t N, K;

			input >> N >> K;

			auto retval = solve(N, K);

			std::cout << "Case #" << i << ": " << retval.first << " " << retval.second << std::endl;
		}
	}
	return 0;
}
