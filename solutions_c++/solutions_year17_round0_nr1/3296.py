#include <iostream>
using namespace std;

int main () {
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti ++) {
		string s;
		int k;
		int ans = 0;
		cin >> s >> k;
		for (int i = 0; i <= s.size() - k; i ++) {
			if (s[i] == '-') {
				ans ++;
				for (int j = i; j < i + k; j ++) {
					s[j] = s[j] == '+' ? '-' : '+';
				}
			}
		}
		for (int i = s.size() - k + 1; i < s.size(); i ++) {
			if (s[i] == '-') {
				ans = -1;
			}
		}
		if (ans != -1) {
			cout << "Case #" << ti << ": " << ans << endl;
		} else {
			cout << "Case #" << ti << ": IMPOSSIBLE" << endl; 
		}
	}
}