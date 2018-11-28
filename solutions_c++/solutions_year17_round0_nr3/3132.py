#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <iostream>
#include <string>


using namespace std;


void solve_single_C() {
	long long n;
	long long k;
	cin >> n >> k;
	long long max_pow = 1;
	int exp = 0;
	while (max_pow * 2 < k + 1) {
		exp++;
		max_pow *= 2;
	}
	long long div = (n + 1) / max_pow;
	long long res = (n + 1) % max_pow;
	long long long_seg = res;
	long long short_seg = max_pow - res;
	long long operation_rest = k - max_pow + 1;
	if (operation_rest <= long_seg) {
		cout << (div + 2) / 2 - 1 << ' ' << (div + 1) / 2 - 1<< endl;
	}
	else {
		cout << (div + 1) / 2 - 1 << ' ' << (div) / 2 - 1 << endl;
	}
}

bool check_tidy(string str) {
	for (int i = 0; i < str.size() - 1; ++i) {
		if (str[i] > str[i + 1]) {
			return false;
		}
	}
	return true;
}

void solve_single_B() {
	string str;
	cin >> str;
	if (check_tidy(str)) {
		cout << str << endl;
		return;
	}
	for (int i = str.size() - 2; i >= 0; --i) {
		string new_str = str;
		if (str[i] == '0') {
			continue;
		}
		new_str[i] = str[i] - 1;
		for (int j = i + 1; j < str.size(); ++j) {
			new_str[j] = '9';
		}
		if (check_tidy(new_str)) {
			if (new_str[0] == '0') {
				new_str = new_str.substr(1, new_str.size() - 1);
			}
			cout << new_str << endl;
			return;
		}
	}
}

void solve_single_A() {
	string str;
	int k;
	cin >> str >> k;
	int ans = 0;
	for (int i = 0; i <= str.size() - k; ++i) {
		if (str[i] == '-') {
			ans++;
			for (int j = i; j < i + k; ++j) {
				if (str[j] == '-') {
					str[j] = '+';
				}
				else {
					str[j] = '-';
				}
			}
		}
	}
	for (int i = 0; i < str.size(); ++i) {
		if (str[i] != '+') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << ans << endl;
	return;
}

int main () {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve_single_C();
	}
	return 0;
};
