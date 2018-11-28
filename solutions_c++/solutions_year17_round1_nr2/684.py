#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
int const N = 1111;
int a[N];
int r[N][N];
int b[N][N], c[N][N];
int pos[N], idx;
bool vis[N][N];
int sel[N];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large-ans.out", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		clr(b, 0xff); idx = 0; clr(vis, 0);
		int n, p; scanf("%d%d", &n, &p);
		rep(i, n) scanf("%d", &a[i]);
		rep(i, n) rep(j, p) scanf("%d", &r[i][j]);
		rep(i, n) rep(j, p) {
			int t = r[i][j];
			int high = t * 10 / a[i] / 9;	
			int low = t * 10 / a[i] / 11;
			if (t * 10 > low * a[i] * 11) ++low;
			if (low > high) low = high = -1;
			b[i][j] = low, c[i][j] = high;
			if (low != -1) pos[idx++] = low;
			//printf("[%d %d] ", low, high); if(j==p-1)puts("");
		}
		int ans = 0;
		sort(pos, pos + idx);
		rep(z, idx) {
			int low = pos[z];
			bool ok = 1;
			rep(i, n) {
				int e = -1, mr = inf;
				rep(j, p) if (!vis[i][j]) {
					if (b[i][j] <= low && c[i][j] >= low) {
						if (c[i][j] < mr) {
							mr = c[i][j]; e = j;
						}
					}
				}
				if (e != -1) {
					sel[i] = e;
				} else {
					ok = 0; break;
				}
			}
			if (ok) {
				rep(i, n) {
					vis[i][sel[i]] = 1;
				}
				++ans;
			}
			
		}
		
		printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}


