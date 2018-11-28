#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void solve() {
	int D, N;
	cin >> D >> N;
	vi K(N), S(N);
	rep(i,0,N) cin >> K[i] >> S[i];
	double ans = 1e100;
	rep(i,0,N) {
		double left = D - K[i];
		double thetime = left / S[i];
		ans = min(ans, D / thetime);
	}
	cout << fixed << setprecision(10) << ans << endl;
}

int main() {
	cin.sync_with_stdio(0);
	cin.exceptions(cin.failbit);

	int TC;
	cin >> TC;
	rep(i,0,TC) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
}
