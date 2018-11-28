#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iomanip>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

typedef pair<int, int> pii;
typedef long long ll;

int c[2][1000] = {};

int N, C, M;

int get(int b, int used = -1) {
	int best = -1;
	int bc = 0;
	int bo = 0;
	REP(i, N) if (i != used) {
		int cur = c[b][i];
		int other = c[!b][i];
		if (cur > 0) {
			if (best == -1 && bo  == 0) {
				best = i;
			}
			if (other > bo) {
				best = i;
				bo = other;
			}
		}
	}
	return best;
}

void solve() {
	REP(i, 1000) {
		c[0][i] = 0;
		c[1][i] = 0;
	}
	cin >> N >> C >> M;
	REP(i, M) {
		int p, b;
		cin >> p >> b;
		b--;
		p--;
		c[b][p]++;
		// if (p > 2) cout << "ERR" ;
	}
	// REP(i,2) {
		// REP(j,5) {
			// cout << c[i][j] << ' ';
		// }
		// cout << endl;
	// }
	int used = 0;
	int ra = 0;
	int rb = 0;
	while (M > used) {
		int ga = c[0][0] ? 0 : get(0);
		if (ga == -1) {
			// cout << "a not found" << endl;
			c[1][get(1)]--;
			used++;
			ra++;
		} else {
			int gb = (ga != 0 && c[1][0]) ? 0 : get(1, ga);
			if (gb == -1) {
				if (ga != 0) {
					gb = get(1);
					if (gb != -1) {
						rb++;
						used++;
					}
				}
			} else {
				used++;
			}
			if (gb != -1) {
				c[1][gb]--;
			}
			c[0][ga]--;
			used++;
			ra++;
		}
	}
	cout << ra << ' ' << rb;
}

int main() {
	int t;
	cin >> t;
	cout << fixed << setprecision(10);
	REP(i, t) {
		cout << "Case #" << (i+1) << ": ";
		solve();
		cout << endl;
	}
}