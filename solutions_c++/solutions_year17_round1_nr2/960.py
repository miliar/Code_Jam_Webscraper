#include <bits/stdtr1c++.h>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef complex<ld> pt;

const int N = 55;
pair<int, int> a[N][N];
int req[N];
int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ": ";
		int n, p; cin >> n >> p;
		for (int i = 0; i < n; i++) {
			cin >> req[i];
		}
		
		// x <= y/(0.9 t), x >= y/(1.1 t) - 1
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) {
				int Q;  cin >> Q;
				int r = Q / ( 0.9 * req[i] ), l = (10 * Q + 11 * req[i] - 1) / ( 11 * req[i] );
				
				if (l <= r) {
					a[i][j] = pii(r,l);
				} else {
					a[i][j] = pii(0,0);
				}
			}
			sort(&a[i][0], &a[i][0]+p);
			reverse(&a[i][0], &a[i][0]+p);
			
			//for (int j = 0; j < p; j++) {
			//	cerr << "(" << a[i][j].first << "," << a[i][j].second << ") ";
			//}
			//cerr << endl;
		}
		//cerr << endl;
		
		int ptr[n], cmax = 0, ans = 0;
		memset(ptr, 0, sizeof ptr);
		while (cmax < p) {
			pii avail = a[0][ptr[0]];
			//cerr << cmax << " " << avail.first << " " << avail.second << endl;
			int best = -1, id = 0;
			for (int i = 0; i < n; i++) {
				if (avail.second < a[i][ptr[i]].second) {
					avail.second = a[i][ptr[i]].second;
				}
				if (avail.first > a[i][ptr[i]].first) {
					avail.first = a[i][ptr[i]].first;
				}
				if (a[i][ptr[i]].second > best) {
					best = a[i][ptr[i]].second;
					id = i;
				}
			}
			
			if (avail.second <= avail.first) {
				if (avail.second != 0) ans++;// += avail.second;
				//cerr << avail.second << endl;
				for (int i = 0; i < n; i++) {
					ptr[i]++;
				}
			} else {
				ptr[id]++;
			}
			
			for (int i = 0; i < n; i++) {
				cmax = max(ptr[i], cmax);
			}
		}
		cout << ans << endl;
    }
	return 0;
}