#include <bits/stdc++.h>
using namespace::std;

int main() {
	int t, caseno = 0;
	cin >> t;
	while (t--) {
		caseno++;
		string a;
		int flips = 0, k, i;
		cin >> a >> k;
		for (i = 0; i < a.size() - k + 1; i++) {
			if (a[i] == '-') {
				flips++;
				for (int j = i; j < i + k; j++) {
					if (a[j] == '-')
						a[j] = '+';
					else
						a[j] = '-';
				}
			}
		}
		for (; i < a.size(); i++)
			if (a[i] == '-')
				flips = -1;
		cout << "Case #" << caseno << ": ";
		if (flips == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << flips << endl;
	}
	return 0;
}
