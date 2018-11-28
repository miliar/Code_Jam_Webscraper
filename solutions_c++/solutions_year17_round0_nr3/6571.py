/*/**/
#include <bits/stdc++.h>

using namespace std;

int a[1021];

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		int n, k;
		cin >> n >> k;
		int l = 0, r = 0;
		memset(a, 0, sizeof a);
		while(k--) {
			int pos = 0;
			l = 0, r = 0;
			for(int i = 0; i < n; i++) {
				if(a[i]) {
					continue;
				}
				int x = i + 1;
				int nl = 0, nr = 0;
				while(x < n) {
					if(a[x]) {
						break;
					}
					else {
						nr++;
						x++;
					}
				}
				x = i - 1;
				while(x >= 0) {
					if(a[x]) {
						break;
					}
					else {
						nl++;
						x--;
					}
				}
				if(min(nl, nr) > min(l, r)) {
					pos = i;
					l = nl;
					r = nr;
				}
				else if(min(nl, nr) == min(l, r) and max(nl, nr) > max(l, r)) {
					pos = i;
					l = nl;
					r = nr;
				}
			}
			a[pos] = 1;
		}
		cout << "Case #" << tc << ": ";
		cout << max(l, r) << " " << min(l, r) << endl;
	}
	return 0;
}