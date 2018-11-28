#include <iostream>
#include <string>

using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for (int p = 1; p <= t; ++p) {
		string s;
		int k;
		cin >> s >> k;
		int cnt = 0;
		int l = s.length();
		int bit[l];
		for (int i = 0; i < l; ++i) {
			if (s[i] == '-') bit[i] = 0;
			else bit[i] = 1;
		}
		int i = 0;
		bool doable = true;
		while (doable && (i < l)) {
			while ((i < l) && (bit[i] == 1)) ++i;
			if (i < l) {
				cnt++;
				if (i + k > l) doable = false;
				else {
					for (int j = i; j < i + k; ++j)
						bit[j] = 1 - bit[j];
					i++;
				}
			}
		}
		cout << "Case #" << p << ": ";
		if (doable) {
			cout << cnt << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
