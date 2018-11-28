#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;

vector<int> get_digits(long long x) {
	vector<int> res;
	while (x > 0) {
		res.push_back(x % 10);
		x /= 10;
	}
	reverse(res.begin(), res.end());
	return res;
}

long long get_number(vector<int> digits) {
	long long x = 0;
	for (int i = 0; i < (int)digits.size(); ++i) {
		x *= 10;
		x += digits[i];
	}
	return x;
}

inline bool good(long long x) {
	vector<int> digits = get_digits(x);
	for (int i = 0; i + 1 < (int)digits.size(); ++i) {
		if (digits[i] > digits[i + 1]) {
			return false;
		}
	}
	return true;
}

long long slow_solve(long long x) {
	while (!good(x)) x--;
	return x;
}

long long solve(long long x) {
	vector<int> digits = get_digits(x);
	if (good(x)) return x;
	vector<int> only_9s((int)digits.size() - 1, 9);
	long long res = get_number(only_9s);
	assert(res <= x);
	for (int change = (int)digits.size() - 1; change >= 0; --change) {
		for (int new_digit = 0; new_digit < digits[change]; ++new_digit) {
			vector<int> cur_digits = get_digits(x);
			cur_digits[change] = new_digit;
			for (int j = change + 1; j < (int) digits.size(); ++j)
				cur_digits[j] = 9;
			long long candidate = get_number(cur_digits);
			if (candidate <= x && good(candidate)) {
				res = max(res, candidate);
			}
		}
	}
	return res;
}

void stress_test() {
	//for (int i = 1; i <= 100000; ++i) {
	//	assert(slow_solve(i) == solve(i));
	//	if (i % 100 == 0)
	//		cout << i << endl;
	//}
	for (int i = 0; i < 100; ++i) {
		int x = (rand() % 10000000) + 1;
		assert(slow_solve(x) == solve(x));
		cout << i << endl;
	}
}

int main() {
	int testsCount;
	cin >> testsCount;
	for (int test = 0; test < testsCount; ++test) {
		long long x;
		cin >> x;
		cout << "Case #" << test + 1 << ": " << solve(x) << endl;
	}
	return 0;
}