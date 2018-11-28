/*/**/
#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		int n;
		cin >> n;
		cout << "Case #" << tc << ": ";
		for(int i = n; i; i--) {
			int x = i;
			int f = x % 10;
			x /= 10;
			int bad = false;
			while(x) {
				int l = x % 10;
				if(f < l) {
					bad = true;
					break;
				}
				f = l;
				 x /= 10;
			}
			if(not bad) {
				cout << i << endl;
				break;
			}
		}
	}
	return 0;
}