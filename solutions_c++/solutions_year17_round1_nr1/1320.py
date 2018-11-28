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
		cout << "Case #" << ttt << ":\n";
		int r, c;
		cin >> r >> c;
		vector<string> s(r);
		for (int i = 0; i < r; i++) {
			cin >> s[i];
		}
		for (int i = 0; i < r; i++) {
			for (int j = 1; j < c; j++) {
				if (s[i][j] == '?' and s[i][j - 1] != '?') {
					s[i][j] = s[i][j - 1];
				}
			}
			for (int j = c - 1; j > 0; j--) {
				if (s[i][j - 1] == '?' and s[i][j] != '?') {
					s[i][j - 1] = s[i][j];
				}
			}
		}
		for (int i = 1; i < r; i++) {
			if (s[i][0] == '?' and s[i - 1][0] != '?') {
				for (int j = 0; j < c; j++) {
					s[i][j] = s[i - 1][j];
				}
			}
		}
		for (int i = r - 1; i > 0; i--) {
			if (s[i - 1][0] == '?' and s[i][0] != '?') {
				for (int j = 0; j < c; j++) {
					s[i - 1][j] = s[i][j];
				}
			}
		}
		for (int i = 0; i < r; i++) {
			cout << s[i] << "\n";
		}
	}
}
