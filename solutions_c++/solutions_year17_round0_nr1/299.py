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

string str;
int k;

void run() {
	cin >> str >> k;
	int n = sz(str);
	vector<int> v(n + 1, 0);
	int flip = 0;
	int ans = 0;
	rep(i, n) {
		flip ^= v[i];
		int cur = (str[i] == '+' ? 1 : 0);
		if(!(cur ^ flip)) {
			if(i + k > n) {
				cout << "IMPOSSIBLE" << endl;
				return;
			}
			ans++;
			flip ^= 1;
			v[i + k] = 1;
		}
	}
	cout << ans << endl;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int tt; cin >> tt;
	for(int tc = 1; tc <= tt; tc++) {
		cout << "Case #" << tc << ": ";
		run();
	}

	return 0;
}

