#include <iostream>
#include <string>
#include <algorithm> 

struct R {
	uint64_t y;
	uint64_t z;
};

R calc(uint64_t N, uint64_t K) {
	uint64_t nleft = (N - 1) / 2;
	uint64_t nright = N / 2;

	if (K == 1) {
		return R{ nright, nleft };
	}

	uint64_t kleft = (K-1) / 2;
	uint64_t kright = K / 2;

	if (kleft != kright) {
		return calc(nright, kright);
	}
	return calc(nleft, kleft);
}

int main(int argc, char** argv) {
	int T;
	std::cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		std::cout << "Case #" << tc << ": ";
		uint64_t N, K;
		std::cin >> N >> K;
		
		R r = calc(N, K);

		std::cout << r.y << ' ' << r.z << '\n';
	}

	return 0;
}