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
int pp[1111], bb[1111];
int g[1111][1111];
int sum[1111][1111];
int num[1111];
int const N = 100100;
int const M = 2222222;
int T;
int n, m;
struct edges{ int u, c, f, next; } e[M];
int p[N], idx;
void addedge(int u, int v, int c, int f) {
	//printf("add(%d,%d,%d,%d)\n",u,v,c,f);
  e[idx].u = v, e[idx].c = c, e[idx].f =  f, e[idx].next = p[u], p[u] = idx++;
  e[idx].u = u, e[idx].c = 0, e[idx].f = -f, e[idx].next = p[v], p[v] = idx++;
}
void init() { idx = 0; clr(p, 0xff); }
struct SSP {
  int mc, mf;
  int pre[N][2], Q[N], dis[N]; bool vis[N];
  bool spfa(int s, int t) {
    clr(dis, 0x3f), clr(vis, 0); dis[s] = 0, Q[0] = s, vis[s] = 1;
    int u, v, w;
    for (int l = 0, h = 1; l != h; ) {
      vis[u = Q[l++]] = 0; if (l == N) l = 0;
      for (int i = p[u]; ~i; i = e[i].next) {
        v = e[i].u, w = e[i].f;
        if (e[i].c && dis[u] + w < dis[v]) {
          dis[v] = dis[u] + w;
          pre[v][0] = u, pre[v][1] = i;
          if (!vis[v]) {
            vis[v] = 1;
            Q[h++] = v; if (h == N) h = 0;
          }
        }
      }
    }
    return dis[t] != inf; // return dis[t] < 0: any flow
  }
  void solve(int s, int t) {
    mc = mf = 0; int u, step;
    while (spfa(s, t)) {
      step = inf;
      for (u = t; u != s; u = pre[u][0]) {
        step = min(step, e[pre[u][1]].c);
      }
      for (u = t; u != s; u = pre[u][0]) {
        e[pre[u][1]].c -= step;
        e[pre[u][1] ^ 1].c += step;
      }
      mf += step;
      mc += dis[t] * step;
    }
  }
} mcf;

int main() {
  freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-ans2.out", "w", stdout);
	int ca = 1; scanf("%d", &T);
	while (T--) {
		//cerr<<T<<endl;
		int nn, c, mm; scanf("%d%d%d", &nn, &c, &mm);
		Rep(i, mm) {
			scanf("%d%d", &pp[i], &bb[i]);
		}
		clr(g, 0); clr(sum, 0); clr(num, 0);
		Rep(i, mm) { g[bb[i]][pp[i]]++; num[bb[i]]++;}
		Rep(i, c) for (int j = nn; j >= 1; --j) {
			sum[i][j - 1] = sum[i][j] + g[i][j];
		}
		int r1 = 0, r2 = 0;
		int mx = 0; Rep(i, c) mx = max(mx, num[i]);
		int low = mx, high = mm, mid;
		while (low <= high) {
			mid = (low + high) / 2;
			init();
		
			int S = c + nn + 1;
			int T = c + nn + 2;
			n = T;
			Rep(i, c) {
				addedge(S, i, num[i], 0);
			}
			Rep(i, c) Rep(j, nn) {
				if (g[i][j] > 0) {
					addedge(i, c + j, g[i][j], 0);
				}
				if (sum[i][j] > 0) {
					addedge(i, c + j, sum[i][j], 1);
				}
			}
			Rep(i, nn) {
				addedge(c + i, T, mid, 0);
			}
			mcf.solve(S, T);
			//cout<<mcf.mc<<" "<<mcf.mf<<endl;
			if (mcf.mf == mm) {
				r1 = mid; r2 = mcf.mc;
			 	high = mid - 1;
			} else {
				low = mid + 1;
			}
		}
		printf("Case #%d: %d %d\n", ca++, r1, r2);
	}
	return 0;
}

