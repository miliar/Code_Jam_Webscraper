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

#define LOCAL
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
		ll n;
		cin >> n;
		vector<ll> digits;
		while (n) {
			digits.pb(n % 10);
			n /= 10;
		}
		int k = SZ(digits);
		for (int ile = 0; ile < 20; ile++) {
			int gdzie = 0;
			for (int i = 1; i < k; i++) {
				if (digits[i] > digits[i - 1]) {
					gdzie = i;
				}
			}
			if (gdzie) {
				digits[gdzie]--;
				for (int i = 0; i < gdzie; i++) {
					digits[i] = 9;
				}
			}
		}
		for (int i = k - 1; i >= 0; i--) {
			n *= 10;
			n += digits[i];
		}
		cout << n << "\n";
	}
}
