#include <iostream>
#include <string>
 
 using namespace std;
 
 int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		string s;
		int K;
		cin >> s >> K;
		int res = 0;
		int j = 0;
		for (; j < s.length() - K + 1; ++j) {
			if (s[j] == '-') {
				++res;
				for (int p = 1; p < K; ++p) {
					s[j + p] = (s[j + p] == '-') ? '+' : '-';
				}
			}
		}
		while (j < s.length()) {
			if (s[j] != '+') {
				cout << "Case #" << i + 1 << ": IMPOSSIBLE\n";
				break;
			}
			++j;
		}
		if (j == s.length()) {
			cout << "Case #" << i + 1 << ": " << res << endl;
		}
	}
 	return 0;
 }
