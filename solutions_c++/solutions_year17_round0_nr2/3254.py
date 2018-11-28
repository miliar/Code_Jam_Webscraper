#include <iostream>
using namespace std;

int main () {
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti ++) {
		string s, ans = "";
		cin >> s;
		int n = s.size();

		for (int i = n-2; i >= 0; i --) {
			if (s[i] > s[i+1]) {
				s[i] --;
				for (int j = i+1; j < n; j ++) {
					s[j] = '9';
				}
			}
		}
		int lo = 0;
		while (s[lo] == '0')
			lo ++;
		for (; lo < n; lo ++)
			ans += s[lo];
		

		// if (ans != -1) {
			cout << "Case #" << ti << ": " << ans << endl;
		// } else {
		// 	cout << "Case #" << ti << ": IMPOSSIBLE" << endl; 
		// }
	}
}