#include <iostream>
#include <string>
#include <cassert>

void decrease(std::string & N, size_t p) {
	if ('0' < N[p]) {
		--N[p];
	} else {
		N[p] = '9';
		decrease(N, p-1);
	}
}

std::string find_last_tidy_number_till(std::string & N)
{
	N.length();
	size_t p = 0;
	while (p < N.length()-1) {
		if (N[p+1] < N[p]) {
			decrease(N, p);
			for (size_t i = p+1; i < N.length(); ++i) {
				N[i] = '9';
			}
			p = 0;
		} else {
			++p;
		}
	}
	size_t first_digit_pos = N.find_first_not_of('0');
	N.erase(0, first_digit_pos);
	return N.empty() ? "0" : N;
}

int main()
{
	size_t T;
	std::string N;

	std::cin >> T;
	assert(T <= 100);

	for (size_t i = 0; i < T; ++i) {
		std::cin >> N;
		assert(0 < N.length());
		assert(N.length() < 20);
		std::cout << "Case #" << i+1 << ": " << find_last_tidy_number_till(N) << std::endl;
	}
	return 0;
}

