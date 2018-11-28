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
using ull = unsigned long long;
int main() {
int t;
	cin >> t;
	FOR(i,1,t+1) {
		ull n, k;
		cin >> n >> k;
		deque<pair<ull, ull>> qu;
		qu.push_back(mp(n, 1));
		while (qu.front().second < k) {
			pair<ull, ull> p = qu.front();
			qu.pop_front();
			if (p.first % 2 == 1) {
				ull neu = p.first / 2;
				ull neuCount = p.second * 2;
				if (qu.back().first == neu) {
					qu.back().second += neuCount;
				} else {
					qu.push_back(mp(neu, neuCount));
				}
			} else {
				ull neu1 = p.first / 2;
				ull neuCount = p.second;
				if (qu.back().first == neu1) {
					qu.back().second += neuCount;
				} else {
					qu.push_back(mp(neu1, neuCount));
				}
				ull neu2 = neu1 - 1;
				qu.push_back(mp(neu2, p.second));
			}
			k -= p.second;
		}
		pair<ull, ull> p = qu.front();
		cout << "Case #" << i << ": " << (p.first / 2) << " " << ((p.first - 1) / 2) << endl;
	}
}
