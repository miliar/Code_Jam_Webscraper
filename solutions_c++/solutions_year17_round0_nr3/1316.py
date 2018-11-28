#define F(n) Fi(i,n)
#define Fi(i,n) Fl(i,0,n)
#define Fl(i,l,n) for(int i=(l);i<(n);++i)
#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/priority_queue.hpp>
using namespace std;
// using namespace __gnu_pbds;
typedef long long ll;
int T;
ll N, K, mn[64], mx[64], nmn[64], nmx[64], ans, ansmin, ansmax;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> T;
	Fl (cases, 1, T + 1) {
		cin >> N >> K;
		mn[0] = mx[0] = N;
		for (int i = 0 ; mn[i] > 0 || mx[i] > 0 ; ++i) {
			mn[i+1] = (mn[i] - 1) >> 1;
			mx[i+1] = mx[i] - 1 - ((mx[i] - 1) >> 1);
			// cout << "JIZZ[" << i << "]: " << mn[i] << " " <<  mx[i] << '\n';
		}
		nmn[0] = 1, nmx[0] = 0;
		for (int i = 0 ; mn[i] > 0 || mx[i] > 0 ; ++i) {
			if (mn[i] & 1) {
				nmn[i + 1] = nmn[i] * 2 + nmx[i];
				nmx[i + 1] = nmx[i];
			} else {
				nmn[i + 1] = nmn[i];
				nmx[i + 1] = nmx[i] * 2 + nmn[i];
			}
			// cout << "NUM[" << i+1 << "]: " << nmn[i+1] << " " <<  nmx[i+1] << '\n';
			// cout << "JIZ[" << i+1 << "]: " << mn[i+1] << " " <<  mx[i+1] << '\n';
		}
		for (int i = 0 ; K > 0 ; ++i) {
			K -= nmx[i];
			if (K <= 0) {
				ans = mx[i];
				break;
			}
			K -= nmn[i];
			if (K <= 0) {
				ans = mn[i];
				break;
			}
		}
		// cout << "JIZZ: " << ans << '\n';
		ansmin = (ans - 1) >> 1;
		ansmax = ans - 1 - ansmin;
		cout << "Case #" << cases << ": " << ansmax << ' ' << ansmin << '\n';
	}
}