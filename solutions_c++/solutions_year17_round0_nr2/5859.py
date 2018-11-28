#include <iostream>
#include <cstdio>
#include <string>
#include <cassert>

void Tidify(std::string::iterator Begin, std::string::iterator Iter, std::string::iterator End) {
	while (Begin != Iter && *Iter == '0') {
		--Iter;
	}

	assert(*Iter != '0');

	*Iter = (*Iter) - 1;

	for (Iter++; Iter != End; Iter++) {
		*Iter = '9';
	}
}

std::string FindMaxTidy(std::string N) {
	for (auto iter = N.begin(); iter + 1 != N.end(); iter++) {
		if (*iter > *(iter + 1)) {
			Tidify(N.begin(), iter, N.end());
			while (!N.empty() && '0' == N[0]) {
				N.erase(0, 1);
			}

			assert(!N.empty());
			return FindMaxTidy(N);
		}
	}

	return N;
}

int main() {
	int T;

	std::cin >> T;

	for (int i = 1; i <= T; i++) {
		std::string N;

		std::cin >> N;

		std::string MaxTidy = FindMaxTidy(N);

		printf("Case #%d: %s\n", i, MaxTidy.data());
	}
}
