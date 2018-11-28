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

size_t count;

void rotate(size_t K, std::string& S, size_t index) {
	for (size_t i = 0; i < K; i++) {
		S[index + i] = (S[index + i] == '-') ? '+' : '-';
	}
	count++;
}

std::string parse(size_t K, std::string S) {
	count = 0;
	auto length = S.size();
	auto goal = std::string(length, '+');
	while (S != goal) {
		for (size_t i = 0; i < length; i++) {
			if (S[i] == '-') {
				if (length - i >= K) {
					rotate(K, S, i);
				} else {
					return "IMPOSSIBLE";
				}
			}
		}
	}

	return std::to_string(count);
}

int main(int, char**) {
	size_t T, i = 0;
	std::string S;
	size_t K;

	std::cin >> T;
	for (size_t i = 0; i < T; i++) {
		std::cin >> S >> K;
		auto answer = parse(K, S);
		std::cout << "Case #" << (i+1) << ": " << answer << std::endl;
	}
}
