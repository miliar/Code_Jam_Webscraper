#include <iostream>
#include <string>
using namespace std;

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
		int count = 0;

		unsigned k;
		string S;
		cin >> S >> k;

		size_t length = S.length();
		bool* pancakes = new bool[length];

		for (size_t i = 0; i < length; ++i) {
			if (S[i] == '+')
				pancakes[i] = true;
			else
				pancakes[i] = false;
		}

		for (size_t i = 0; i < length - k + 1; ++i) {
			if (!pancakes[i]) {
				++count;
				for (size_t j = 0; j < k; ++j)
					pancakes[i + j] = !pancakes[i + j];
			}
		}

		bool impossible = false;
		for (size_t i = length - k + 1; i < length; ++i) {
			if (!pancakes[i]) {
				impossible = true;
				break;
			}
		}

		if (impossible)
			printf("Case #%u: IMPOSSIBLE\n", caseIndex);
		else
			printf("Case #%u: %i\n", caseIndex, count);
	}
}
