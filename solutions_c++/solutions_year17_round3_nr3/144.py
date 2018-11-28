#include <bits/stdtr1c++.h>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef complex<ld> pt;

// dp(n, k, U) := best prob on nth, k done, U units left.
// 50 * 50 * 10000 * 10000

// for K = N case, we want to maximize

// prod (xi + ui) s.t. sum ui == U, ui >= 0.

// (x+a)(y+u-a) == -a^2 + au - ax + ay + ux + xy
// best a --> f' = -2a + u - x + y = 0
// a = (y + u - x) / 2
// objective: (u + x + y)^2 / 4 it seems.
// so u is spread so that every probability is made equal.

// d/dui = prod (xj + uj) / (xi + ui) - prod ( xj + uj ) / (xn + un) - lambda = 0
// --> (xn + un) / (xi + ui) = 1 for every xi.

// if i only need k i should just train the best k
// if i train the best, i need to make as even as possible.

int n, k;
ld a[55], memo[55][55];
ld dp(int i, int j) {
	if (j == k) return 1;
	if (i == n) return 0;
	if (memo[i][j] >= 0) return memo[i][j];
	
	ld& ans = memo[i][j] = 0;
	ans = (1 - a[i]) * dp(i+1, j) + a[i] * dp(i+1, j+1);
	return ans;
}

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ": ";
		
		memset(a, 0, sizeof a);
		ld u, sum = 0; 
		cin >> n >> k >> u;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			sum += 1.0 - a[i];
		}
		a[n] = 1.0;
		u = min(u, sum);
		
		const ld eps = 1e-8;
		while (u > eps) {
			sort(a, a+n);
			int i = 0;
			while (i + 1 < n && abs(a[i] - a[i+1]) < eps) {
				i++;
			}
			i++;
			
			ld incr = min( (a[i] - a[0]) / i, u / i );
			for (int j = 0; j < i; j++) {
				a[j] += incr;
				u -= incr;
				a[j] = min( 1.0L, a[j] );
			}
		}
		for (int i = 0; i < n; i++) {
			cerr << a[i] << " ";
		}
		cerr << endl << endl;
		
		for (int i = 0; i < 55; i++) {
			for (int j = 0; j < 55; j++) {
				memo[i][j] = -1;
			}
		}
		cout << fixed << setprecision(10) << dp(0, 0) << endl;
    }
	return 0;
}