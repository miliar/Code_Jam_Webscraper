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
		int n, c, m;
		cin >> n >> c >> m;
		vector<vector<int>> C(2, vector<int>(n));
		rep (i, 0, m) {
			int p, b;
			cin >> p >> b;
			C[b - 1][p - 1]++;
		}
		if (c != 2) {
			cout << "-1";
			continue;
		}
		int sC[2] = {0, 0};
		rep (i, 0, 2) {
			rep (j, 0, n) {
				sC[i] += C[i][j];
			}
		}
		int wyn = 0, p = 0;
		rep (x, 0, 2000) {
			rep (j, 1, n) {
				rep (i, 0, 2) {
					while (C[i][j] > sC[!i] - C[!i][j]) {
						DBG(i, j, C[i][j], C[!i][j], sC[!i]);
						if (C[!i][j] == 0) {
							wyn++;
							sC[i]--;
							C[i][j]--;
							break;
						}
						sC[0]--;
						sC[1]--;
						C[i][j]--;
						C[!i][j]--;
						p++;
						wyn++;
					}
				}
			}
		}
		DBG(C[0][0], C[0][1], sC[0], sC[1], wyn, p);
		wyn += C[0][0];
		sC[1] = max(sC[1] - C[0][0], 0);
		sC[0] -= C[0][0];
		wyn += C[1][0];
		sC[0] = max(sC[0] - C[1][0], 0);
		sC[1] -= C[1][0];
		DBG(sC[0], sC[1]);
		wyn += max(sC[0], sC[1]);
		cout << wyn << " " << p << "\n";
	}
}
