#include <iostream>
#include <string>

using namespace std;

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		string S;
		string ans;
		cin >> S;
		// find largest non-increasing prefix
		int i = 0;
		while (i + 1 < S.size() && S[i + 1] >= S[i]) {
			++i;
		}
		ans = S;
		if (i != S.size() - 1) {
			char last_digit = S[i];
			if (last_digit == '1') {
				ans = string(S.size() - 1, '9');
			} else {
				int j = i;
				while (j > 0 && S[j - 1] == last_digit) {
					--j;
				}
				--ans[j];
				for (j = j + 1; j < ans.size(); ++j) {
					ans[j] = '9';
				}
			}
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}
