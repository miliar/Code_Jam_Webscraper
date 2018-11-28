#include <bits/stdc++.h>
using namespace std;

void main2() {
	string s;
	cin >> s;
	int k;
	cin >> k;
	int cnt = 0;
	for (int i = 0; i+k-1 < (int)s.size(); i++) if (s[i] == '-') {
		for (int j = 0; j < k; j++)
			s[i+j] = '+' + '-' - s[i+j];
		cnt++;
	}
	if (s.find('-') == s.npos)
		cout << cnt << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}

int main() {
	int t;
	cin >> t;
	for (int o = 1; o <= t; o++) {
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
