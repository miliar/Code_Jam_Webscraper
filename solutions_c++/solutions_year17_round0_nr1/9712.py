#include <bits/stdc++.h>
#include <fstream>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;
typedef vector<ll> V;
typedef complex<double> Point;

#define PI acos(-1.0)
#define EPS 1e-10
const ll INF = 1e9 + 7;
const ll MOD = 1e9 + 7;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,N) for(int i=0;i<(N);i++)
#define ALL(s) (s).begin(),(s).end()
#define EQ(a,b) (abs((a)-(b))<EPS)
#define EQV(a,b) ( EQ((a).real(), (b).real()) && EQ((a).imag(), (b).imag()) )
#define fi first
#define se second

int t;
string s;
int k;

int solve() {
	int res = 0;
	REP(i, s.size() - (k - 1)) {
		//cout << res << endl;
		if (s[i] == '-') {
			res++;
			REP(j, k) {
				if (s[i + j] == '-') s[i + j] = '+';
				else s[i + j] = '-';
			}
		}
	}
	FOR(i, s.size() - (k - 1), s.size()) {
		if (s[i] == '-')return -1;
	}
	return res;
}

int main() {
	ofstream ans;
	ifstream r;
	r.open("A-small-attempt3.in");
	ans.open("A-ans.out");
	r >> t;
	REP(i, t) {
		ans << "Case #" << i + 1 << ": ";
		r >> s >> k;
		int num = solve();
		if (num == -1) ans << "IMPOSSIBLE" << endl;
		else ans << num << endl;;
	}
}