#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, k;
	string x;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		int c = 0;
		cin >> x >> k;
		for (int i = 0; i <= x.length() - k; i++) {
			if (x[i] == '-') {
				c++;
				for (int j = i; j < i + k; j++)
					x[j] = x[j] == '-' ? '+' : '-';
			}
		}
		for (int i = x.length() - k; i < x.length(); i++)
			if (x[i] == '-')
				c = -1;
		if (c == -1)
			cout << "Case #" << tt << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << tt << ": " << c << "\n";
	}
	return 0;
}
