#include <iostream>

using namespace std;

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ti++) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		for (int j = 0; j < s.size(); j++) {
			if (s[j] == '-' && j + k <= s.size()) {
				ans++;
				for (int l = j; l < j + k; l++) {
					if (s[l] == '-') {
						s[l] = '+';
					} else {
						s[l] = '-';
					}
				}
			}
		}
		bool happy = true;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-')
				happy = false;
		}
		if (happy == false) {
			cout << "Case #" << ti << ": IMPOSSIBLE" << endl;	
		}
		else {
			cout << "Case #" << ti << ": " << ans << endl;
		}
	}

}
