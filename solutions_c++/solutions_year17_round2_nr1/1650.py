#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
 
#define ECHO(x) std::cout << x << std::endl;
#define TRACE(x) std::cout << (#x) << " = " << (x) << std::endl;

using vecl = std::vector<long>;

double parse(long D, const vecl& K, const vecl& S) {
	long N = K.size();
	double biggestTimeToReach = 0;
	for (size_t i = 0; i < N; i++) {
		auto speed = S[i];
		auto pos = K[i];
		auto remaining = D - pos;
		auto timeToReach = ((double) remaining) / speed;
		if (timeToReach > biggestTimeToReach) {
			biggestTimeToReach = timeToReach;
		}
	}

	return D / biggestTimeToReach;
}

int main(int, char**) {
	size_t T, i = 0;
	long D, N;
	vecl K, S;

	std::cin >> T;
	for (size_t i = 0; i < T; i++) {
		std::cin >> D >> N;
		K.resize(N);
		S.resize(N);
		for (size_t j = 0; j < N; j++) {
			std::cin >> K[j] >> S[j];
		}
		auto answer = parse(D, K, S);
		// std::cout << "Case #" << (i+1) << ": " << answer << std::endl;
		printf("Case #%d: %.20f\n", i+1, answer);
	}
}
