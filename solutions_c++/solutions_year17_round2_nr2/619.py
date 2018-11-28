#include <bits/stdc++.h>                 // [PRIMES]               1777 ~2^10.80
using namespace std;                     //                       10333 ~2^13.33
using ll = long long;                    // seq 1 128 | factor   100333 ~2^16.61
using vl = vector<ll>;                   //   | grep -v ' .* '  1300111 ~2^20.31
using vvl = vector<vl>;                  //                    10300777 ~2^23.30
using pll = pair<ll,ll>;                 //                   100400999 ~2^26.58
using vb = vector<bool>;                 //                  1300400999 ~2^30.28
const ll oo = 0x3f3f3f3f3f3f3f3fLL;      //                 10200500333 ~2^33.25
const double eps = 1e-9;                 //                100200400777 ~2^36.54
#define sz(c) ll((c).size())             //               1200300700111 ~2^40.13
#define all(c) begin(c),end(c)           //              10200300500777 ~2^43.21
#define mp make_pair                     //             100200300400777 ~2^46.51
#define mt make_tuple                    //            1200300400600999 ~2^50.09
#define pb push_back                     //           10200300400600111 ~2^53.18
#define eb emplace_back                  //          100200300400600333 ~2^56.48
#define xx first                         //         1200300400500800999 ~2^60.06
#define yy second
#define has(c,i) ((c).find(i) != end(c))
#define FOR(i,a,b) for (int i=(a); i<(b); i++)
#define FORD(i,a,b) for (int i=int(b)-1; i>=(a); i--)
void fail() {
	cout << "IMPOSSIBLE" <<endl;
}
int n, r, o, y, g, b, v;
vl cs(3);
int prefer, last;
char getNext() {
	static const vector<char> x = {'R', 'Y', 'B'};
	int maxi = -1;
	FOR(i, 0, 3) {
		if (last != i && cs[i] > 0) {
			if (maxi == -1 || cs[maxi] < cs[i]) {
				maxi = i;
			} else if (cs[maxi] == cs[i] && prefer == i) {
				maxi = i;
			}
		}
	}
	if (maxi == -1) {
		return '#';
	}
	cs[maxi]--;
	if (prefer == -1) prefer = maxi;
	last = maxi;
	return x[maxi];
}
int main() {
	int tc;
	cin >> tc;
	FOR(tt, 1, tc+1) {
		cout << "Case #" << tt << ": ";

		cin >> n >> r >> o >> y >> g >> b >> v;

		// special case
		string res;
		if (n == r + g && r == g) {
			FOR(q, 0, g) res += "GR";
			cout << res << endl;
			continue;
		}
		if (n == y + v && y == v) {
			FOR(q, 0, y) res += "YV";
			cout << res << endl;
			continue;
		}
		if (n == b + o && b == o) {
			FOR(q, 0, b) res += "BO";
			cout << res << endl;
			continue;
		}

		cs[0] = r;
		cs[1] = y;
		cs[2] = b;
		prefer = -1;
		char c = -1;
		last = -1;
		FOR(nn, 0, r + y + b) {
			c = getNext();
			if (c == '#') {
				break;
			} else {
				res += c;
				if (c  == 'R' && g > 0) {
					if (cs[0] < g) {
						break;
					} else {
						FOR(q, 0, g) res += "GR";
						cs[0] -= g;
						nn += g;
					}
				}

				if (c  == 'Y' && v > 0) {
					if (cs[1] < v) {
						break;
					} else {
						FOR(q, 0, v) res += "VY";
						cs[1] -= v;
						nn += v;
					}
				}

				if (c  == 'B' && o > 0) {
					if (cs[2] < o) {
						break;
					} else {
						FOR(q, 0, o) res += "OB";
						cs[2] -= o;
						nn += o;
					}
				}
			}
		}
		if (res.length() < n) {
			fail(); continue; // failed
		}
		if (last == prefer) {
			fail();
		} else {
			cout << res << endl;
		}
	}
}
