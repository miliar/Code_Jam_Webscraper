#include <algorithm>
#include <iomanip>
#include <istream>
#include <map>
#include <numeric>
#include <ostream>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <random>
#include <complex>
#include <functional>
#include <cstdarg>
#include <cstdio>
#include <stack>
#include <limits>
#include <tuple>

using namespace std;


namespace caide {


typedef long long ll;


}


using namespace caide;

// Powered by caide (code generator, tester, and library code inliner)

class Solution {
public:
	ll INF = numeric_limits<ll>::max();

    void solve(std::istream& in, std::ostream& out) {
		int T; in >> T;
		for (int test = 1; test <= T; ++test) {
			ll hd, ad, hk, ak, b, d; in >> hd >> ad >> hk >> ak >> b >> d;
			ll res = INF;
			for (int nd = 0; nd <= ak; ++nd) {
				for (int nb = 0; nb <= hk; ++nb) {
					res = min(res, solve(hd, ad, hk, ak, b, d, nb, nd));
				}
			}
			out << "Case #" << test << ": ";
			if (res == INF)
				out << "IMPOSSIBLE";
			else
				out << res;
			out << endl;
		}
    }

	ll solve(ll hd, ll ad, ll hk, ll ak, ll b, ll d, ll nb, ll nd) {
		ll maxhd = hd;
		bool healing = false;
		ll res = 0;
		while (nd) {
			if (hd <= ak-d) {
				if (healing)
					return INF;
				healing = true;
				hd = maxhd - ak;
				++res;
				continue;
			}
			healing = false;
			ak -= d;
			if (ak < 0)
				ak = 0;
			hd -= ak;
			++res;
			--nd;
		}

		healing = false;
		while (nb) {
			if (hd <= ak) {
				if (healing)
					return INF;
				healing = true;
				hd = maxhd - ak;
				++res;
				continue;
			}
			healing = false;
			ad += b;
			hd -= ak;
			++res;
			--nb;
		}

		healing = false;
		while (hk > ad) {
			if (hd <= ak) {
				if (healing)
					return INF;
				healing = true;
				hd = maxhd;
				++res;
				hd -= ak;
				continue;
			}
			healing = false;
			hk -= ad;
			hd -= ak;
			++res;
		}

		return res + 1;
	}
};

void solve(std::istream& in, std::ostream& out)
{
    out << std::setprecision(12);
    Solution solution;
    solution.solve(in, out);
}


#include <fstream>
#include <iostream>


int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);


    istream& in = cin;


    ostream& out = cout;

    solve(in, out);
    return 0;
}


#include <cstdlib>


