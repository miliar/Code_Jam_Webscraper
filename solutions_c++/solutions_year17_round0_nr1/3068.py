#include <iostream>
#include <string>
#include <vector>

using namespace std;

string invert(string s, int k, int f) {
	for (int i = f; i < f+k; i++) {
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
	return s;
}

int main() {
	int t, k, j;
	int f, l;
	string s;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> s >> k;
		f = 0;
		l = s.size()-1;
		int ans = 0;
		bool imp = false;
		while(1) {
			while(f < s.size() && s[f] != '-') {
				f++;
			}
			while(l >= 0 && s[l] != '-') {
				l--;
			}
			if(f >= s.size() || l < 0) {
				break;
			}
			if(l-f+1 < k) {
				imp = true;
				break;
			}
			s = invert(s, k, f);
			ans++;
		}
		if(imp) {
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << i+1 << ": " << ans << endl;
		}
	}
	return 0;
}