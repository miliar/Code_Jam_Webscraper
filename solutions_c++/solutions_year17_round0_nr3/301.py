// .... .... .....!
// ...... ......!
// .... ....... ..... ..!
// ...... ... ... .... ... .... .....!
// ... .. ... .... ...?

#include<bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define sz(x) (int((x).size()))
#define pb push_back
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second
//#define endl '\n'

template<class P, class Q> inline void smin(P &a, Q b) { if (b < a) a = b; }
template<class P, class Q> inline void smax(P &a, Q b) { if (a < b) a = b; }

typedef long long ll;
typedef pair<int, int> pii;

////////////////////////////////////////////////////////////////////////////////

void run() {
	ll n, k;
	cin >> n >> k; k--;
	ll a = 0, b = 1;
	while (a + b <= k) {
		k -= a + b;
		if(n / 2 == (n-1) / 2) b += a + b; else a += a + b;
		n /= 2;
	}
	if(k < b) cout << n/2 << ' ' << (n-1)/2 << endl;
	else cout << (n-1)/2 << ' ' << (n-2)/2 << endl;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int tt; cin >> tt;
	for(int tc = 1; tc <= tt; tc++) {
		cerr << "running test #" << tc << ".. " << endl;

		cout << "Case #" << tc << ": ";
		run();
	}

	return 0;
}
