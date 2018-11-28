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

const int maxn = 50 + 10;
const int maxp = 50 + 10;

int n, p;
int req[maxn];
vector<int> v[maxn];
int pos[maxn];

void run() {
	cin >> n >> p;
	rep(i, n) cin >> req[i];
	rep(i, n) rep(j, p) {
		int x; cin >> x;
		v[i].pb(x);
	}

	rep(i, n) sort(all(v[i]));

	int ans = 0;
	while(1) {
		bool can = true;
		int mn = 0;
		rep(i, n) {
			if(pos[i] == sz(v[i])) { can = false; break; }
			int val = v[i][pos[i]];
			smax(mn, ((val * 10 + 10) / 11 + req[i] - 1) / req[i]);
		}
		if(!can) break;
		rep(i, n) {
			int val = v[i][pos[i]];
			if(val * 10 < mn * req[i] * 9) {
				pos[i]++;
				can = false;
			}
		}
		if(can) {
			rep(i, n) pos[i]++;
			ans++;
		}
	}
	cout << ans << endl;
}

void case_init() {
	rep(i, maxn) v[i].clear(), pos[i] = 0;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int tt; cin >> tt;
	for(int tc = 1; tc <= tt; tc++) {
		cerr << " ** running test #" << tc << ".. **" << endl;

		int before = clock();
		case_init();

		cout << "Case #" << tc << ": ";
		run();
		cerr << " -- time = " << clock() - before << endl;
	}

	return 0;
}

