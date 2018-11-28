#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int testcase;
	cin >> testcase;
	for (int t = 1; t <= testcase; t++) {
		long long n;
		int p = 0, flag, j = 0;
		cin >> n;
		string s;
		while (n != 0) {
			int m = n % 10;
			n = n / 10;
			s.insert(p, 1, m + '0');
			p++;
		}
		reverse(s.begin(), s.end());
		flag = p;
		for (int i = 0; i < s.length() - 1; i++) {
			if (s[i] > s[i + 1]) {
				flag = i + 1;
				s[i] -= 1;
				break;
			}
		}
		for (int i = flag; i < s.length(); i++) {
			s[i] = '9';
		}
		for (int i = flag - 1; i > 0; i--) {
			if (s[i] < s[i - 1]) {
				s[i] = '9';
				s[i - 1] -= 1;
			}
		}
		for (int i = 0; i < s.length(); i++) {
			if (s[i] != '0') {
				j = i;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		for (int i = j; i < s.length(); i++) {
			cout << s[i];
		}
		cout << endl;
	}
	return 0;
}