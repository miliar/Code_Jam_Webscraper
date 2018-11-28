#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

bool tidy(long N) {
	int p = N % 10;
	N /= 10;
	while (N > 0) {
		int c = N % 10;
		if (c > p) {
			return false;
		}
		N /= 10;
		p = c;
	}
	return true;
}

int naive_max_tidy(long N) {
	while (!tidy(N)) {
		--N;
	}
	return N;
}

std::vector<int> get_digits(long N) {
	std::vector<int> v;
	while (N > 0) {
		v.push_back(N % 10);
		N /= 10;
	}
	std::reverse(v.begin(), v.end());
	return v;
}

int find_violation(const std::vector<int>& digits) {
	for (int i = 1; i < digits.size(); ++i) {
		if (digits[i-1] > digits[i]) {
			return i - 1;
		}
	}
	return -1;
}

long build_next(const std::vector<int> digits, const int& k) {
	long newN = 0;
	for (int i = 0; i < k; i++) {
		newN = 10 * newN + digits[i];
	}
	newN = 10 * newN + (digits[k]-1);
	for (int i = k+1; i < digits.size(); i++) {
		newN = 10 * newN + 9;
	}
	return newN;
}

long efficient_max_tidy(long N) {
	int k = -1;
	do {
		std::vector<int> digits = get_digits(N);
		k = find_violation(digits);
		if (k != -1) {
			N = build_next(digits, k);
		}
	} while(k != -1);
	return N;
}

int main(int argc, char** argv) {
        std::ifstream fin(argv[1], std::ifstream::in);

        int t;
        fin >> t;

	for (int i = 1; i <= t; i++) {
		long N;
		fin >> N;

		std::cout << "Case #" << i << ": " << efficient_max_tidy(N) << std::endl;
	}

	return 0;
}

