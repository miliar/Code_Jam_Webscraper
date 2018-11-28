#include <iostream>
#include <string>

using namespace std;
int main() {
	int t; cin >> t;

	for (int i_t = 1; i_t <= t; ++i_t) {
		string s;
		cin >> s;
		while (true) {
			bool flipped = false;
			for (int i = 0; i < s.length() - 1; ++i) {
				if (s[i] > s[i + 1]) {
					flipped = true;
					s[i] = s[i] - 1;
					for (int j = i + 1; j < s.length(); ++j) {
						s[j] = '9';
					}
					if (i == 0) {
						goto out;
					}
				}
			}
			if (!flipped) {
				goto out;
			}
		}
	out:;

		// remove leading zeros
		int leading_count = 0;

		for (int i = 0; i < s.length(); ++i) {
			if (s[i] == '0') {
				leading_count++;
			} else {
				break;
			}
		}
		s.erase(0, leading_count);
		cout << "Case #" << i_t << ": " << s << endl;
	}
	return 0;
}
