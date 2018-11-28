#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

struct State {
	int v0, v1, v2, v3;
	State() {}
	State(int v0, int v1, int v2, int v3) : v0(v0), v1(v1), v2(v2), v3(v3) {}
};

int dis[111][111][111][111];
int hd, ad, hk, ak, b, d;
queue<State> q;

inline void update(State &s, int val) {
	int &src = dis[s.v0][s.v1][s.v2][s.v3];
	if (src == 0x3f3f3f3f) {
		src = val;
		q.push(s);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
		memset(dis, 0x3f, sizeof(dis));
		dis[hd][ad][hk][ak] = 0;
		q.push(State(hd, ad, hk, ak));
		int res = 0x3f3f3f3f;
		while (!q.empty()) {
			State u = q.front(), v;
			q.pop();
			int dd = dis[u.v0][u.v1][u.v2][u.v3] + 1;

			v = u;
			v.v2 = max(0, v.v2 - v.v1);
			v.v0 = max(0, v.v0 - v.v3);
			if (v.v2 == 0) {
				res = dd;
				break;
			} else if (v.v0 > 0) {
				update(v, dd);
			}

			v = u;
			v.v1 = min(100, v.v1 + b);
			v.v0 = max(0, v.v0 - v.v3);
			if (v.v0 > 0) {
				update(v, dd);
			}

			v = u;
			v.v0 = hd;
			v.v0 = max(0, v.v0 - v.v3);
			if (v.v0 > 0) {
				update(v, dd);
			}

			v = u;
			v.v3 = max(0, v.v3 - d);
			v.v0 = max(0, v.v0 - v.v3);
			if (v.v0 > 0) {
				update(v, dd);
			}
		}
		while (!q.empty()) {
			q.pop();
		}
		printf("Case #%d: ", kase);
		if (res == 0x3f3f3f3f) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", res);
		}
	}
	return 0;
}
