// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>
#include <complex>

using namespace std;

#define rep(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template<typename T> inline bool smin(T &a, const T &b)   { return a > b ? a = b : a;    }
template<typename T> inline bool smax(T &a, const T &b)   { return a < b ? a = b : a;    }

typedef long long LL;

const int N = (int) 1e5 + 5, mod = (int) 0;
pair<int, int> to_decr[6] = {{0, 3}, {1, 4}, {2, 5}, {0, 1}, {1, 2}, {0, 2}};
int tmp[6][6], adj[6][6], sn, sr, so, sy, sg, sb, sv;
int check(string s) {
	int cr = 0, co = 0, cy = 0, cg = 0, cb = 0, cv = 0;
	for (auto ch : s) {
		if (ch == 'O') {
			++co;
		} else if (ch == 'R') {
			++cr;
		} else if (ch == 'B') {
			++cb;
		} else if (ch == 'Y') {
			++cy;
		} else if (ch == 'G') {
			++cg;
		} else if (ch == 'V') {
			++cv;
		} else {
			return 0;
		}
	}
	for (int j = 0; j < (int) s.size(); ++j) {
		if (s[j] == s[j + 1]) return 0;
		if (s[j] == 'O') {
			if (j >= 1 && s[j - 1] != 'B') return 0;
			if (j + 1 != s.size() && s[j + 1] != 'B') return 0;
		}
		if (s[j] == 'G') {
			if (j >= 1 && s[j - 1] != 'R') return 0;
			if (j + 1 != s.size() && s[j + 1] != 'R') return 0;
		}
		if (s[j] == 'V') {
			if (j >= 1 && s[j - 1] != 'Y') return 0;
			if (j + 1 != s.size() && s[j + 1] != 'Y') return 0;
		}
	}
	if (cv != sv) return 0;
	if (cg != sg) return 0;
	if (cy != sy) return 0;
	if (cr != sr) return 0;
	if (cb != sb) return 0;
	if (co != so) return 0;
	return 1;
}
char ch[6];
int t, ss[N];
void dfs(int v) {
	for (int u = 0; u < 6; ++u) {
		int x = min(u, v), y = max(u, v);
		if (adj[x][y] > 0) {
			adj[x][y]--;
			dfs(u);
		}
	}
	ss[t++] = v;
}
int main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt << ": ";
		int n, a, ab, b, bc, c, ac;

		cin >> n >> a >> ab >> b >> bc >> c >> ac;
		sn = n;
		sr = a;
		so = ab;
		sy = b;
		sg = bc;
		sb = c;
		sv = ac;
		ch[0] = 'R';
		ch[3] = 'G';
		ch[1] = 'Y';
		ch[4] = 'V';
		ch[2] = 'B';
		ch[5] = 'O';
		memset(tmp, 0, sizeof tmp);
		memset(adj, 0, sizeof adj);
		tmp[0][3] = bc * 2;
		tmp[1][4] = ac * 2;
		tmp[2][5] = ab * 2;
		c -= ab;
		b -= ac;
		a -= bc;
		string res = "IMPOSSIBLE";
		if (a >= 0 && b >= 0 && c >= 0) {
			for (int a_b = 0; a_b <= 2 * n; ++a_b) {
				int a_c = 2 * a - a_b;
				int b_c = 2 * b - a_b;
				if (a_c < 0 || b_c < 0) continue;
				if (a_c + b_c != 2 * c) continue;
				tmp[0][1] = a_b;
				tmp[1][2] = b_c;
				tmp[0][2] = a_c;
				memcpy(adj, tmp, sizeof adj);
//				for (int z = -1; z <= 1; z += 2)
//					for (int p = -1; p <= 1; p += 2)
				for (int dec0 = 0; dec0 < 7; ++dec0) {
					for (int dec1 = 0; dec1 < 7; ++dec1) {
						memcpy(adj, tmp, sizeof adj);
						if (dec0 != 6) adj[to_decr[dec0].first][to_decr[dec0].second] --;
						if (dec1 != 6) adj[to_decr[dec1].first][to_decr[dec1].second] --;
						int odd = 0;
						int ok = 1;
						for (int x = 0; x < 6 && ok; ++x) {
							int deg = 0;
							for (int y = 0; y < 6 && ok; ++y) {
								if (adj[x][y] < 0 || adj[y][x] < 0) ok = 0;
								deg += adj[x][y], deg += adj[y][x];
							}
							if (ok) {
								if (deg % 2 == 1) odd = x;
							}
						}
						if (ok) {
							t = 0;
							dfs(odd);
							string cur = "";
		//					if (t == n - 1) {
							//	int st = odd;
								for (int j = 0; j < t; ++j) {
									cur += ch[ss[j]];
							//		if (j != t) {
							//			st ^= ss[j];
							//		}
								}
								if (check(cur)) {
									res = cur;
								}
		//					}
						}
						
					}
				}
			}
		}
		
		cout << res << endl;
	}
}

















