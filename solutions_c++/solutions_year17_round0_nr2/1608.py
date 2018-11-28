#include <iostream>

using namespace std;

string nines(int n) {
	string result = "";
	for (int i = 0; i < n; i++) {
		result += '9';
	}
	return result;
}

bool all_zeros(string s) {
	for (int i = 0; i < s.length(); i++) {
		if (s[i] != '0') {
			return false;
		}
	}
	return true;
}

/* bool check(int a) {
	int l = a % 10;
	a /= 10;
	while (a) {
		int c = a % 10;
		a /= 10;
		if (c > l) {
			return false;
		}
		l = c;
	}
	return true;
}

int naive(int a) {
	while (a) {
		if (check(a)) return a;
		a--;
	}
}

string int_to_str(int a) {
	string s = "";
	while (a) {
		s = (char) ((a % 10) + '0') + s;
		a /= 10;
	}
	return s;
} */

int main() {
	int t;
	cin >> t;
	for (int _t = 0; _t < t; _t++) {
		string num;
		cin >> num;
		int k = num.length();
		for (int i = 0; i < num.length() - 1; i++) {
			if (num[i] > num[i + 1]) {
				k = i + 1;
				char c = num[i];
				num[i] = c - 1;
				for (int j = i - 1; j >= 0 && num[j] == c; j--) {
					num[j + 1] = '9';
					num[j] = c - 1;
				}
				break;
			}
		}
		cout << "Case #" << (_t + 1) << ": ";
		string s1 = num.substr(0, k);
		if (all_zeros(s1)) {
			s1 = nines(k - 1);
		}
		string ans = s1 + nines(num.length() - k);
		ans.erase(0, ans.find_first_not_of('0'));
		cout << ans << endl;
	}
}
