#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
	
	int T, K;
	string s;

	cin >> T;

	for (int k = 1; k <= T; ++k) {
		cin >> s >> K;

		int minimum = 0;
		int i;
		for (i = 0; i <= s.length()-K; ++i) {
			if(s[i] == '-') {
				++minimum;
				for (int j = 0; j < K; ++j) {
					if(s[i+j] == '-') {
						s[i+j] = '+';
					} else {
						s[i+j] = '-';
					}
				}
			}
		}

		bool flag = true;
		for ( ; i < s.length(); ++i) {
			if(s[i] == '-') {
				flag = false;
				break;
			}
		}

		cout << "Case #" << k << ": ";
		if(flag) {
			cout << minimum << "\n";
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}

	return 0;
}