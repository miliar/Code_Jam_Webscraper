#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	string x;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		int c = 0;
		cin >> x;
		for (int i = 0; i < x.length() - 1; i++) {
			if (x[i] > x[i + 1]) {
				x[c] = x[c] - 1;
				for (int j = c + 1; j < x.length(); j++)
					x[j] = '9';
				break;
			} else if (x[i] < x[i + 1])
				c = i + 1;
		}
		if (x[0] == '0')
			x = x.substr(1);
		cout << "Case #" << tt << ": " << x << "\n";
	}
	return 0;
}
