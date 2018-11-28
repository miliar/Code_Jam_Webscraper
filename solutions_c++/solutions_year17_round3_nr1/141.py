#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

const int N = 1010;

int n, k;

ii vec[N];

int main(void) {
	int T;
	cin >> T;

	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> k;

		for (int i = 0; i<n ;i++) {
			cin >> vec[i].fi >> vec[i].se;
		}
		sort (vec, vec + n);

		int j = n-1;
		double ansx = 0;

		int kx = k;
		for (int i = n-1; i>=0; i--) {
			j = i;
			double ans = 1.0 * vec[j].fi * vec[j].fi * acos(-1) + 2.0 * acos(-1) * vec[j].fi * vec[j].se;

			if (i+1 < k) break;

			priority_queue<ll> q;
			for (j = i-1; j>=0; --j) {
					q.push(1LL * vec[j].se * vec[j].fi);
			}

			for (j = 1; j<k; j++){
					ans += q.top() * 2.0 * acos(-1);
					q.pop();
			}

			ansx=max(ansx,ans);
		}
		printf("Case #%d: %.9lf\n", tt, ansx);

	}
	
	
	return 0;
}
