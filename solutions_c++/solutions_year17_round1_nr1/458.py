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

const int maxn = 25 + 5;

int n, m;
string s[maxn];

void run() {
	cin >> n >> m;
	rep(i, n) cin >> s[i];

	rep(i, n)
		if(s[i] != string(m, '?')) {
			rep(j, m) if(s[i][j] != '?' && j+1 < m && s[i][j+1] == '?') s[i][j+1] = s[i][j];
			rof(j, m, 1) if(s[i][j] != '?' &&  s[i][j-1] == '?') s[i][j-1] = s[i][j];
		} else if(i && s[i-1][0] != '?')
			s[i] = s[i-1];
	rof(i, n, 1) if(s[i][0] != '?' && s[i-1][0] == '?') s[i-1] = s[i];
	rep(i, n) cout << s[i] << endl;
}

void case_init() {
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int tt; cin >> tt;
	for(int tc = 1; tc <= tt; tc++) {
		cerr << " ** running test #" << tc << ".. **" << endl;

		int before = clock();
		case_init();

		cout << "Case #" << tc << ":" << endl;
		run();
		cerr << " -- time = " << clock() - before << endl;
	}

	return 0;
}

