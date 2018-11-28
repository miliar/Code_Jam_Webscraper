#include<bits/stdc++.h>
#define rep(i,k,n) for(ll i= (ll) k;i< (ll) n;i++)
#define all(v) (v).begin(), (v).end()
#define SZ(v) (int)((v).size())
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;
const int N = 1048576;

using namespace std;

template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
}

//#define LOCAL
#ifdef LOCAL
#define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define DBG(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif

int main() {
    #ifndef LOCAL
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    #endif
    int num_tests;
    cin >> num_tests;
    for (int ttt = 1; ttt <= num_tests; ttt++) {
		cout << "Case #" << ttt << ": ";
		int n, k;
		cin >> n >> k;
		vector<ll> r(n), h(n);
		rep (i, 0, n) {
			cin >> r[i] >> h[i];
		}
		double wyn = 0;
		rep (i, 0, n) {
			ll R = r[i];
			vector<ll> myh;
			rep (j, 0, n) {
				if (j != i and r[j] <= R) {
					myh.pb(h[j] * r[j] * 2);
				}
			}
			if (SZ(myh) < k - 1) {
				continue;
			}
			sort(all(myh));
			ll Pb = h[i] * r[i] * 2;
			for (int j = SZ(myh) - k + 1; j < SZ(myh); j++) {
				Pb += myh[j];
			}
			double new_wyn = double(R * R + Pb) * M_PI;
			if (ttt == 89) {
				DBG(R, Pb, new_wyn, n, k);
			}
			wyn = max(wyn, new_wyn);
		}
		cout << fixed << setprecision(8) << wyn << "\n";
	}
}
