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

const int maxn = 100 + 10;

int n, p;
int c[5];

void run() {
	cin >> n >> p;
	rep(i, n) { int g; cin >> g; c[g % p]++; }

	int ans = c[0];
	c[0] = 0;

	if(p == 2) ans += c[1] / 2, c[1] %= 2;
	if(p == 3) {
		int m = min(c[1], c[2]);
		ans += m, c[1] -= m, c[2] -= m;
		ans += c[1] / 3, c[1] %= 3;
		ans += c[2] / 3, c[2] %= 3;
	}
	if(p == 4) {
		ans += c[2] / 2, c[2] %= 2;
		int m = min(c[1], c[3]);
		ans += m, c[1] -= m, c[3] -= m;
		int k = (c[1] > c[3] ? 1 : 3);
		if(c[k] >= 2 && c[2]) ans++, c[k] -= 2, c[2]--;
		ans += c[1] / 4, c[1] %= 4;
		ans += c[3] / 4, c[3] %= 4;
	}

	if(accumulate(c, c + p, 0) > 0)
		ans++;
	cout << ans << endl;
}

void case_init() {
	rep(i, 5) c[i] = 0;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int start_clock = clock();
	int tt; cin >> tt;
	for(int tc = 1; tc <= tt; tc++) {
		int case_clock = clock();

		cerr << " -------- #" << tc << ".." << endl;
		case_init();
		cout << "Case #" << tc << ": ";
		run();

		cerr.setf(ios::fixed); cerr.precision(6);
		cerr << " -------- [" << ((clock() - case_clock) / (double)CLOCKS_PER_SEC) << " / " <<
			((clock() - start_clock) / (double)CLOCKS_PER_SEC) << "]" << endl;
	}

	return 0;
}

