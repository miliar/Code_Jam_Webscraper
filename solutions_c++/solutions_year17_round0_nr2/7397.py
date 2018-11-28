#include <iostream>
#include <cstdio>
#include <string>
using namespace std;



int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		string s;
		cin >> s;
		for (int i = 1; i < s.length(); i++) {
			if (s[i - 1] > s[i]) {
				for (int j = i - 1; j >= 0; j--) {
					if (j == 0 || s[j - 1] < s[j]) {
						s[j]--;
						for (int k = j + 1; k < s.length(); k++) {
							s[k] = '9';
						}
						while (s[0] == '0') {
							s = s.substr(1, s.length() - 1);
						}
						break;
					}
				}
				break;
			}
		}
		cout << "Case #" << tt << ": " << s << endl;
	}
	return 0;
}