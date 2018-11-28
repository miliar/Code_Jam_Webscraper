#include <iostream>
#include <string>
#include <cassert>

typedef std::pair<bool, size_t> result_t;

void flip(std::string & S, size_t pos, size_t K)
{
	assert(pos + K <= S.length());
	for (; 0 < K; --K, ++pos) {
		char & c = S[pos];
		if ('+' == c) {
			c = '-';
		} else if ('-' == c) {
			c = '+';
		} else {
			assert(!"Invalid character");
		}
	}
}

result_t get_number_of_steps(std::string & S, const size_t K)
{
	size_t number_of_steps = 0;

	size_t pos = S.find('-');
	while (pos <= S.length() - K) {
		flip(S, pos, K);
		++number_of_steps;
		
		pos = S.find('-', pos+1);
	}
	
	return {S.find('-') == std::string::npos, number_of_steps};
}

int main(int argc, char **argv)
{
	size_t T, K;
	std::string S;

	std::cin >> T;
	for (size_t i = 0; i < T;) {
		std::cin >> S >> K;
		
		result_t result = get_number_of_steps(S, K);
		
		assert(2 <= K);
		assert(K <= S.length());
		assert(S.length() <= 1000);
		
		std::cout << "Case #" << ++i << ": ";
		if (result.first) {
			std::cout << result.second;
		} else {
			std::cout << "IMPOSSIBLE";
		}
		std::cout << std::endl;
	}
	return 0;
}

