#include <vector>
#include <iostream>

using namespace std;

size_t digits[18] = { 0 };

bool isTidy(size_t length) {
	for (size_t i = 0; i < length-1; i++) {
		if (digits[i + 1] > digits[i]) return false;
	}

	return true;
}
void updateDigits(size_t length) {
	for (size_t i = 0; i < length; i++) {
		if (digits[i] == 0) {
			digits[i] = 9;
		} else {
			digits[i] -= 1;
			break;
		}
	}
}
// works only for small input numbers
void computeSmall(size_t i, long long number) {
	// reset
	for (size_t i = 0; i < 18; i++) {
		digits[i] = 0;
	}

	// stored the other way round
	size_t length = 0;
	for (; number > 0; length++) {
		// modulo
		long long n = number / 10;
		size_t r = number - n * 10;

		digits[length] = r;

		number = n;
	}

	long long count = 0;
	for (;;) {
		if (isTidy(length)) {
			long long n = 0;
			long long pos = 1;
			for (size_t i = 0; i < 18; i++) {
				n += pos * digits[i];
				pos *= 10;
			}

			cout << "Case #" << i + 1 << ": " << n << endl;
			break;
		}

		updateDigits(length);
		if ((count % 100000000LL) == 0) cout << count << endl;
		count++;
	}
}
void computeBig(size_t i, long long number) {
	// reset
	for (size_t i = 0; i < 18; i++) {
		digits[i] = 0;
	}

	// stored the other way round
	size_t length = 0;
	for (; number > 0; length++) {
		// modulo
		long long n = number / 10;
		size_t r = number - n * 10;

		digits[length] = r;

		number = n;
	}

	// find first untidyness
	for (size_t i = 0; i < length - 1; i++) {
		//for (size_t i = 0; i < length; i++) {
		//	cout << digits[i];
		//}
		//cout << endl;

		if (digits[i + 1] > digits[i]) {
			for (size_t j = 0; j <= i; j++) {
				digits[j] = 9;
			}
			digits[i + 1] -= 1;
		}
	}

	// restore
	long long n = 0;
	long long pos = 1;
	for (size_t i = 0; i < 18; i++) {
		n += pos * digits[i];
		pos *= 10;
	}
	cout << "Case #" << i + 1 << ": " << n << endl;
}

void main() {
	size_t testCount;
	cin >> testCount;

	long long number;
	for (size_t i = 0; i < testCount; i++) {
		cin >> number;
		computeBig(i, number);
		//cout << "---------------" << endl;
	}
}