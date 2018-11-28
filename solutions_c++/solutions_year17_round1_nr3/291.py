#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

int hd, ad, hk, ak, b, d;

void solve()
{
	cin >> hd >> ad >> hk >> ak >> b >> d;
	int best = 10000;
	FOR(nd, 101) {
		FOR(nb, 101) {
			int rounds = 0;
			int ndr = nd;
			int nbr = nb;
			int akc = ak;
			int adc = ad;
			int hdc = hd;
			int hkc = hk;
			while (true) {
				++rounds;
				if (rounds >= 10000) break;
				if (adc >= hkc) break;
				if (akc >= hdc && (ndr == 0 || akc - d >= hdc)) {
					hdc = hd;
				} else if (ndr > 0) {
					akc = max(0, akc - d);
					--ndr;
				} else if (nbr > 0) {
					adc += b;
					--nbr;
				} else {
					hkc -= adc;
				}
				hdc -= akc;
				if (hdc <= 0) {
					rounds = 10000;
					break;
				}
			}
			best = min(best, rounds);
		}
	}
	if (best < 10000) {
		cout << best;
	} else {
		cout << "IMPOSSIBLE";
	}
}

int main()
{
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
