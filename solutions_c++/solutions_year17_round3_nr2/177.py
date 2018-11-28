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

int dp[721][721][2][2];

int main() {
    #ifndef LOCAL
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    #endif
    int num_tests;
    cin >> num_tests;
    for (int ttt = 1; ttt <= num_tests; ttt++) {
		cout << "Case #" << ttt << ": ";
		int Ac, Aj;
		vector<char> kto(1441, '.');
		cin >> Ac >> Aj;
		rep (i, 0, Ac) {
			int a, b;
			cin >> a >> b;
			rep (j, a + 1, b + 1) {
				kto[j] = 'C';
			}
		}
		rep (i, 0, Aj) {
			int a, b;
			cin >> a >> b;
			rep (j, a + 1, b + 1) {
				kto[j] = 'J';
			}
		}
		rep (i, 0, 721) {
			rep (j, 0, 721) {
				dp[i][j][0][0] = IINF;
				dp[i][j][0][1] = IINF;
				dp[i][j][1][0] = IINF;
				dp[i][j][1][1] = IINF;
			}
		}
		if (kto[0] != 'C') {
			dp[1][0][0][0] = 0;
		}
		if (kto[0] != 'J') {
			dp[0][1][1][1] = 0;
		}
		for (int s = 2; s <= 1440; s++) {
			for (int c = max(0, s - 720); c <= min(720, s); c++) {
				int j = s - c;
				//DBG(s, c, j);
				//assert?
				for (int kto_zaczal = 0; kto_zaczal < 2; kto_zaczal++) {
					// moze C?
					if (c != 0 and kto[s] != 'C') {
						dp[c][j][0][kto_zaczal] = min(dp[c][j][0][kto_zaczal], dp[c - 1][j][0][kto_zaczal]);
						dp[c][j][0][kto_zaczal] = min(dp[c][j][0][kto_zaczal], dp[c - 1][j][1][kto_zaczal] + 1);
					}
					// moze J?
					if (j != 0 and kto[s] != 'J') {
						dp[c][j][1][kto_zaczal] = min(dp[c][j][1][kto_zaczal], dp[c][j - 1][1][kto_zaczal]);
						dp[c][j][1][kto_zaczal] = min(dp[c][j][1][kto_zaczal], dp[c][j - 1][0][kto_zaczal] + 1);
					}
				}
			}
		}
		int wyn = IINF;
		wyn = min(wyn, dp[720][720][0][0]);
		wyn = min(wyn, dp[720][720][0][1] + 1);
		wyn = min(wyn, dp[720][720][1][0] + 1);
		wyn = min(wyn, dp[720][720][1][1]);
		cout << wyn << "\n";
	}
}
