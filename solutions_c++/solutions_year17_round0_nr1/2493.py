#include <iostream>

using namespace std;

int canFlip(string s, int k) {
	int n = s.size();
	int out = 0;
	for (int i = 0; i < n; i++) {
		if (s[i] == '-') {
			out++;
			if (i + k > n) return -1;
			for (int j = i + 1; j < i + k; j++) {
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
		} 
	}
	return out;
}

int main()
{
	int t, k; cin >> t;
	for (int c = 1; c <= t; c++) {
		string s;
		cin >> s >> k;
		int x = canFlip(s, k);
		cout << "Case #" << c << ": ";
		if (x >= 0) {
			cout << x;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}