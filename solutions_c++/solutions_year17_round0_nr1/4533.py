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
		string s;
		int k;
		cin >> s >> k;
		int n = SZ(s);
		vector<int> flip(n);
		int nflips = 0, allflips = 0;
		for (int i = 0; i <= n - k; i++) {
			if (i - k >= 0 and flip[i - k]) {
				nflips--;
			}
			bool b = (s[i] == '-') xor (nflips % 2);
			if (b) {
				flip[i] = 1;
				nflips++;
				allflips++;
			}
			DBG(i, flip[i], nflips);
		}
		bool imp = 0;
		for (int i = n - k + 1; i < n; i++) {
			if (i - k >= 0 and flip[i - k]) {
				nflips--;
			}
			DBG(i, nflips);
			bool b = (s[i] == '-') xor (nflips % 2);
			if (b) {
				imp = 1;
				break;
			}
		}
		if (imp) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		cout << allflips << "\n";		 
	}
}
