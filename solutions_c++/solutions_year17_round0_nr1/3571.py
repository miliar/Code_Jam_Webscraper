#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		string s;
		int k;
		cin >> s >> k;
		int n = 0;
		for (int i = 0; i < s.length() - k + 1; i++) {
			if (s[i] == '-') {
				n++;
				for (int j = i; j < i + k; j++) {
					s[j] = s[j] == '+' ? '-' : '+';
				}
			}
		}
		int m = 0;
		for (int i = s.length() - k + 1; i < s.length(); i++) {
			if (s[i] == '-') {
				m++;
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if (m == 0) {
			cout << n << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
