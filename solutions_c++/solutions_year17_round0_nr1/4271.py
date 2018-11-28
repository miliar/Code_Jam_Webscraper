#include <iostream>
#include <string>

using namespace std;
int main() {
	int t; cin >> t;

	for(int i_t = 1; i_t <= t; ++i_t) {
		string s; 
		cin >> s;
		int k;
		cin >> k;
		int flips = 0;
		for (int i = 0; i <= s.length() - k; ++i) {
			if (s[i] == '-') {
				for (int j = 0; j < k; ++j) {
					if (s[i + j] == '-') {
						s[i + j] = '+';
					} else {
						s[i + j] = '-';
					}
				}
				flips++;
			}
		}
		int i = s.length() - 1;
		int lim = s.length() - 1 - k;

		for (; i > lim; --i) {
			if (s[i] == '-') {
				cout << "Case #" << i_t << ": " << "IMPOSSIBLE" << endl;
				goto end;
			}
		}

		cout << "Case #" << i_t << ": " << flips << endl;

	end:;
	}
	return 0;
}