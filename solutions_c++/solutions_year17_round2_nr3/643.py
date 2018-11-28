#include <bits/stdc++.h>                 // [PRIMES]               1777 ~2^10.80
using namespace std;                     //                       10333 ~2^13.33
using ll = long long;                    // seq 1 128 | factor   100333 ~2^16.61
using vl = vector<ll>;                   //   | grep -v ' .* '  1300111 ~2^20.31
using vvl = vector<vl>;                  //                    10300777 ~2^23.30
using vvd = vector<vector<double>>;                  //                    10300777 ~2^23.30
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
struct horseTime {
	ll d, s;
	double t;
};


int main() {
	int tc;
	cin >> tc;
	FOR(tt, 1, tc+1) {
		cout << "Case #" << tt << ":";

		int n, q;
		cin >> n >> q;
		vector<pair<ll, ll>> horse(n);
		FOR(i,0,n) cin >> horse[i].first >> horse[i].second;

		vector<vector<ll>> nex(n, vector<ll>(n));
		FOR(i,0,n) {
			FOR(k, 0, n) {
				ll d;
				cin >> d;
				nex[i][k] = d;
//				if (d != -1) {
//					nex[i].pb(mp(k, d));
//				}
			}
		}

		vvd fl(n, vector<double>(n, 1e300));

		FOR(nn, 0, n) {
			// time, city, rem
			set<tuple<double, int, int>> qu;
			qu.insert(mt(0, nn, horse[nn].first));
			while (!qu.empty()) {
				auto p = *qu.begin();
				ll from = get<1>(p);
//					cerr << from << endl;
				ll rem = get<2>(p);
				qu.erase(qu.begin());
				if (fl[nn][from] + 1 < 1e300) continue; // already
				fl[nn][from] = get<0>(p);
				FOR(k, 0, n) {
					if (from != k && nex[from][k] != -1 && rem >= nex[from][k]) {
						qu.insert(mt(get<0>(p) + nex[from][k] / (double) horse[nn].second, k, rem - nex[from][k]));
					}
				}
			}
		}

		FOR(m, 0, n) FOR(s, 0, n) FOR(e, 0, n) {
			if (m == s || m == e || s == e) continue;
			if (fl[s][e] > fl[s][m] + fl[m][e]) fl[s][e] = fl[s][m] + fl[m][e];
		}

		FOR(qq, 0, q) {
			int a, b;
			cin >> a >> b;
			a--; b--;

			printf(" %.7f", fl[a][b]);
		}

/*
		FOR(qq, 0, q) {
			int a, b;
			cin >> a >> b;
			a--; b--;


			// DO
			vector<horseTime> curHorses;
			curHorses.pb({horse[0].first, horse[0].second, 0});
			double best;
			FOR(nn, 1, n) {
				best = 1e300;
				vector<horseTime> newHorses;
				for (auto & h : curHorses) {
					if (h.d >= nex[nn-1][nn]) {
						double nt = h.t + nex[nn-1][nn] / (double) h.s;
						best = min(best, nt);
						newHorses.pb({h.d - nex[nn-1][nn], h.s, nt});
					}
				}
				curHorses =  newHorses;
				// change
				curHorses.pb({horse[nn].first, horse[nn].second, best});
			}
			printf(" %.7f", best);
		}*/
		cout << endl;
	}
}
