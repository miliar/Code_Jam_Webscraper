#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <string>
#include <cassert>
#include <sstream>
#include <iostream>
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }


bool isTidy(LL x) {
	LL prevDigit = -1;
	while (x > 0) {
		LL digit = x % 10;
		if (prevDigit != -1 && prevDigit < digit) {
			return false;
		}
		prevDigit = digit;
		x /= 10;
	}
	return true;
}
LL simple(LL x) {
	while (true) {
		if (isTidy(x)) {
			return x;
		}
		x -= 1;
	}
}
string toDigits(LL x) {
	string digits;
	while (x > 0) {
		digits.push_back(x % 10);
		x /= 10;
	}
	reverse(digits.begin(), digits.end());
	return digits;
}
LL fromDigits(string digits) {
	LL x = 0;
	for (auto digit : digits) {
		x = x * 10 + digit;
	}
	return x;
}
LL fast(LL x) {
	if (x < 10) {
		return x;
	}
	auto digits = toDigits(x);
	size_t bad_i = string::npos;
	for (size_t i = 1; i < digits.size(); i++) {
		if (digits[i - 1] > digits[i]) {
			bad_i = i;
			break;
		}
	}
	if (bad_i == string::npos) {
		return x;
	}
	digits[bad_i - 1] -= 1;
	fill(digits.begin() + bad_i, digits.end(), 9);
	return fast(fromDigits(digits));
}

void Go() {
	LL n;
	cin >> n;
	cout << fast(n) << endl;
}

int main() {
	const string task = "B";
	const string folder = "gcj/2017/qual";
	const int attempt = -1;
	const bool dbg = false;

	if (dbg) {
		freopen("inp.txt", "r", stdin);
	}
	else {
		stringstream ss;
		ss << folder << '/' << task;
		if (attempt < 0)
			ss << "-large";
		else
			ss << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}
	ios_base::sync_with_stdio(false);

	for (LL x = 1; x < 10000; x++) {
		LL s = simple(x);
		LL f = fast(x);
		if (s != f) {
			throw 1;
		}
	}

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		Go();
	}
	return 0;
}
