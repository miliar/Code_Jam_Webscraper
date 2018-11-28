#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1e3 + 10;

int n,c,m;
int t[N][N],total[N];

inline void update (int id, int k, int x) {
	for (int i = k;i < N;i += i & (-i)) {
		t[id][i] += x;
	}
}

inline int query (int id, int k) {
	int sum = 0;
	for (int i = k;i > 0;i -= i & (-i)) {
		sum += t[id][i];
	}
	return sum;
}

inline int atleast (int id, int k) {
	return total[id] - query (id, k);
}

inline void solve () {
	scanf ("%d %d %d", &n, &c, &m);

	for (int i = 0;i < N;i ++) {
		total[i] = 0;
		for (int j = 0;j < N;j ++) {
			t[i][j] = 0;
		}
	}

	for (int i = 0;i < m;i ++) {
		int p,b;
		scanf ("%d %d", &p, &b);
		b --;
		t[b][p] ++;
		total[b] ++;
	}

	int ans1 = 0,ans2 = 0;
	for (int k = 0;k < 2;k ++) {
		for (int i = 1;i <= n;i ++) {
			for (int j = i + 1;j <= n and t[k][i] > 0;j ++) {
				int x = min (t[k][i], t[k ^ 1][j]);
				t[k][i] -= x;
				t[k ^ 1][j] -= x;
				ans1 += x;
			}
		}
	}
	ans1 += t[0][1] + t[1][1];
	for (int i = 2;i <= n;i ++) {
		ans1 += max (t[0][i], t[1][i]);
		ans2 += min (t[0][i], t[1][i]);
	}
	printf ("%d %d\n", ans1, ans2);
}

int main () {
	int t;
	scanf ("%d", &t);

	for (int i = 1;i <= t;i ++) {
		printf ("Case #%d: ", i);
		solve ();
	}
}