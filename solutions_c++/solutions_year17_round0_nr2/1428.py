#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstdint>

using namespace std;

int main(int argc, char** argv) {
	const unsigned NSIZE = 20;

	unsigned test_count; cin >> test_count;
	unsigned num[NSIZE];
	for (unsigned ti = 1; ti <= test_count; ++ti) {
		uint64_t n; cin >> n;
		fill(num, num + NSIZE, 0);
		uint64_t tmp = n;
		unsigned numsize = 0;
		while (tmp != 0) {
			num[numsize++] = tmp % 10;
			tmp /= 10;
			assert(numsize <= NSIZE);
		}

		for (unsigned i = 0; i < numsize; ++i) {
			for (unsigned j = i + 1; j < numsize; ++j) {
				if (num[i] < num[j]) {
					--num[j];
					fill(num, num + j, 9);
				}
			}
		}

		cout << "Case #" << ti << ": ";
		bool first_zero = true;
		for (unsigned i = 0; i < NSIZE; ++i) {
			if (first_zero && num[NSIZE - i - 1] == 0) continue;
			if (num[NSIZE - i - 1] != 0) first_zero = false;
			cout << num[NSIZE - i - 1];
		}
		cout << endl;
	}

	return 0;
}
