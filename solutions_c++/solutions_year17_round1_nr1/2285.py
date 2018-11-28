#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;


template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }

typedef long long ll;
const int MOD = 1000002013;

const double pi = atan(1.0)*4.0;

const double eps = 1e-8;

ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }

int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int dp[101][2];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

    int T;
    cin >> T;
    for1(tc, T) {
      
        int nr, nc;
	cin >> nr; cin >> nc;
	string grid[nr][nc];
//	grid.resize(nr);
//	forn(i,nr) grid[i].resize(nc);

        forn(i,nr) {
		string tmp;
                cin >> tmp;
		forn(j,nc) {
			grid[i][j] = tmp[j];
		}
	}

        forn(i,nr) {
                forn(j,nc-1) {
                        if (grid[i][j] == "?") {
				if ((grid[i][j+1] != "?")) { 
					grid[i][j] = grid[i][j+1];
					for(int s = j-1; s >= 0; s--) {
                                                if (grid[i][s] == "?") grid[i][s] = grid[i][j];
                                        }
				}
			}
                }
		for(int k = nc-1; k >=1; k--) {
			if (grid[i][k] == "?") {
				if ((grid[i][k-1] != "?")) {
					grid[i][k] = grid[i][k-1];
					for(int s = k+1; s < nc; s++) {
						if (grid[i][s] == "?") grid[i][s] = grid[i][k];
					}
				}
			}
		}
        }

        forn(j,nc) {
                forn(i,nr-1) {
                        if (grid[i][j] == "?") {
                                if ((grid[i+1][j] != "?")) { 
					grid[i][j] = grid[i+1][j];
					for(int s = i-1; s >= 0; s--) {
                                                if (grid[s][j] == "?") grid[s][j] = grid[i][j];
                                        }
				}
                        }
                }
                for(int k = nr-1; k >= 1; k--) {
                        if (grid[k][j] == "?") {
                                if ((grid[k-1][j] != "?")) {
					grid[k][j] = grid[k-1][j];
					for(int s = k+1; s < nr; s++) {
                                                if (grid[s][j] == "?") grid[s][j] = grid[k][j];
                                        }
				}
                        }
                }
        }
/*
	forn(i,nr) {
		forn(j,nc) {
			cout << grid[i][j];
		}
		cout << endl;
	}
*/
	cout << "Case #" << tc << ": " << endl;
	forn(i,nr) {
                forn(j,nc) {
                        cout << grid[i][j];
                }
                cout << endl;
        }
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
