#include <bits/stdc++.h>
using namespace std;

typedef long double ld;
typedef pair<ld,ld> ii;

#define _USE_MATH_DEFINES
#define fi first
#define se second

long long T, n, k, r, h;

ii p[1005];


int main() {

	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n >> k;
		for (int i = 1; i <= n; i++) {
			cin >> r >> h;
			
			// top, side area
			p[i] = {M_PI * r * r, 2 * M_PI * r * h};
		}

		sort(p + 1, p + n + 1);

		priority_queue<ld,vector<ld>,greater<ld>> pq;

		long double best_side = 0.0;
		for (int i = 1; i < k; i++) {
			best_side += p[i].se;
			pq.push(p[i].se);
		}

		long double best_ans = 0.0;
		for (int i = k; i <= n; i++) {
			best_ans = max(best_ans, best_side + p[i].fi + p[i].se);
			pq.push(p[i].se); best_side += p[i].se;
			best_side -= pq.top(); pq.pop();
		}

		cout << "Case #" << t << ": " << fixed << setprecision(10) << best_ans << endl;
	}

	return 0;
}