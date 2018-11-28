#include <iostream>
#include <algorithm>

std::string solve(std::string N) {
	// remove first 0s
	bool front = true;
	N.erase(std::remove_if(N.begin(), N.end(), [&](char n) {
		if (n != '0') front = false;
		return front;
	}), N.end());

	bool done = false;
	for (size_t i = 1 ; i < N.size() ; ++i) {
		if (done) N[i] = '9';
		if (N[i-1] <= N[i]) continue;
		N[i] = '9';
		size_t k = i-1;
		while(N[k] == '0') {
			N[k] = '9';
			--k;
		}
		N[k]--;
		done = true;
	}
	if (done) return solve(N);
	return N;
}

int main(int argc, const char *argv[])
{
	int T;
	std::string N;

	std::cin >> T;
	for (int tcase = 1 ; tcase <= T ; ++tcase) {
		std::cout << "Case #" << tcase << ": ";
		std::cin >> N;
		std::cout << solve(N) << std::endl;
	}
	return 0;
}
