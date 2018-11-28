#include <bits/stdc++.h>


#define puba push_back
#define ff first
#define ss second
#define pii pair <int, int>


using namespace std;


typedef long long LL;


int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";
		
		LL n, k;
		cin >> n >> k;
		map <LL, LL> segs;
		segs[n] = 1;
		while (true) {
			pair <LL, LL> cur = *segs.rbegin();
			segs.erase(cur.ff);



			if (cur.ss >= k) {
				cout << cur.ff / 2 << " ";
				if (cur.ff & 1) cout << cur.ff / 2;
				else cout << cur.ff / 2 - 1;
				break;
			}
			else {
				segs[cur.ff / 2] += cur.ss;
				LL tmp = cur.ff / 2;
				if ((cur.ff & 1) == 0) --tmp;
				if (tmp > 0) {
					segs[tmp] += cur.ss;		
				}
				k -= cur.ss;
			}
		}

		cout << endl;
	}
	return 0;
}