#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;
typedef pair<ii,int> iii;
#define _USE_MATH_DEFINES
#define fi first
#define se second

int T, n, m, k, r, h, s, de;

iii a[1000];


int main() {

	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n >> m;

		int nLeft = 720, mLeft = 720;

		for (int i = 0; i < n; i++) {
			cin >> s >> de;

			mLeft -= de - s;
			a[i] = iii(ii(s, de), 0);
		}

		for (int i = 0; i < m; i++) {
			cin >> s >> de;

			nLeft -= de - s;
			a[n+i] = iii(ii(s, de), 1);
		}

		sort(a, a + n + m);

		int ans = 0;

		priority_queue<int,vector<int>,greater<int>> pq[2];
		for (int i = 0; i + 1 < n + m; i++) {
			if (a[i].se == a[i+1].se) {
				pq[a[i].se].push(a[i+1].fi.fi - a[i].fi.se);
				//cout << a[i].se << " " << a[i+1].fi.fi - a[i].fi.se << endl;
			} else {
				ans++;
			}
		}

		if (a[0].se == a[n+m-1].se) {
			pq[a[0].se].push(1440 - a[n+m-1].fi.se + a[0].fi.fi);
			//cout << a[0].se << " " << 1440 - a[n+m-1].fi.se + a[0].fi.fi << endl;
		} else {
			ans++;
		}

		while (mLeft >= 0) {
			if (!pq[0].empty() && pq[0].top() <= mLeft) {
				mLeft -= pq[0].top(); pq[0].pop();// ans-=2;
			} else {
				break;
			}
		}

		ans += 2 * pq[0].size();

		while (nLeft >= 0) {
			if (!pq[1].empty() && pq[1].top() <= nLeft) {
				nLeft -= pq[1].top(); pq[1].pop(); //ans-=2;
			} else {
				break;
			}
		}

		ans += 2 * pq[1].size();

		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}