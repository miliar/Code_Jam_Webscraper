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
const int IINF = 1e9 + 1;
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
		int n, p;
		cin >> n >> p;
		vector<int> X(4);
		rep (i, 0, n) {
			int x; 
			cin >> x;
			X[x % p]++;
		}
		if (p == 2) {
			cout << X[0] + X[1] / 2 + X[1] % 2 << "\n";
		}
		if (p == 3) {
			int m = min(X[1], X[2]);
			int d = max(X[1], X[2]) - min(X[1], X[2]);
			DBG(m ,d);
			cout << X[0] + m + d / 3 + (d % 3 > 0) << "\n";
		}
		if (p == 4) {
			int m = min(X[1], X[3]);
			int d = max(X[1], X[3]) - min(X[1], X[3]);
			DBG(m ,d);
			int wyn = X[0] + X[2] / 2 + m;
			if (X[2] % 2 == 1) {
				if (d >= 2) {
					wyn++;
					d -= 2;
					cout << wyn + d / 4 + (d % 4 > 0) << "\n";
				} else {
					cout << wyn + 1 << "\n";
				}
			} else {
				cout << wyn + d / 4 + (d % 4 > 0) << "\n";
			}
		}
	}
}
