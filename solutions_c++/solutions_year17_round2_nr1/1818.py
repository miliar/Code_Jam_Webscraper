#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<ll> vll;
typedef pair<ll, ll> pll;

const ll oo = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-9;

#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define FORD(i,a,b) for (ll i = ll(b)-1; i >= (a); i--)

#define sz(c) ll((c).size())
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define xx first
#define yy second

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(nullptr);

	int T;
	cin >> T;
	FOR(z, 0, T){
		ll D, N;
		cin >> D >> N;


		ld slowest = 0;
		vector<pair<ll, ll>> horses(N);

		FOR(i, 0, N){
			ll t, y;
			cin >> t >> y;
			horses[i] = {t, y};

		}

		FOR(i, 0, N){
			ld x, y;
			tie(x, y) = horses[i];
			ld time = (D - x) / ((ld) y);
			slowest = max(slowest, time);
		}

		cout << "Case #" << z+1 << ": " << setprecision(10) << fixed << D / slowest << endl;

	}

	return 0;
}
