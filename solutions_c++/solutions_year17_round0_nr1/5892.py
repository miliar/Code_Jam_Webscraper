#include <string>
#include <iostream>
#include <utility>
#include <algorithm>

std::pair<bool, int> operator+(const int &Lhs, const std::pair<bool, int> &Rhs) {
	return {Rhs.first, Rhs.second + Lhs};
}

char Flip(char Ch) {
	if ('+' == Ch) {
		return '-';
	} else {
		return '+';
	}
}

std::pair<bool, int> Solve(std::string::iterator Begin, std::string::iterator End, int K) {
	if (Begin == End) {
		return {true, 0};
	} else if (End - Begin < K) {
		return {std::all_of(Begin, End, [](char Ch) { return '+' == Ch; }), 0};
	}

	if (*Begin == '+') {
		return Solve(Begin + 1, End, K);
	} else {
		for (int i = 0; i < K; i++) {
			*(Begin + i) = Flip(*(Begin + i));
		}

		return 1 + Solve(Begin + 1, End, K);
	}
}

int main() {
	int T;

	std::cin >> T;

	for (int i = 1; i <= T; i++) {
		int K;
		std::string S;

		std::cin >> S >> K;

		std::pair<bool, int> Result = Solve(S.begin(), S.end(), K);

		printf("Case #%d: ", i);
		if (true == Result.first) {
			printf("%d", Result.second);
		} else {
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}

	return 0;
}
