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

int main() {

	int t;
	cin >> t;
	FOR(i,1,t+1) {
		string s;
		cin >> s;
		char first = s[0];
		int x = 1;
		while (x < s.length() && s[x] >= s[x-1]) x++;
		if (x != s.length()) {
			int y = x - 2;
			s[x-1]--;
			while (y >= 0 && s[y] > s[x-1]) {
				s[y] = s[x-1];
				y--;
			}
			if (y == -1 && s[0] == '0') {
				cout << "Case #" << i << ": ";
				FOR(k, 1, s.length()) {
					cout << '9';
				}
				cout << endl;
				continue;
			}
			y+=2;
			while (y < s.length()) {
				s[y] = '9';
				y++;
			}
		}
		printf("Case #%d: %s\n", i, s.c_str());
	}
}
