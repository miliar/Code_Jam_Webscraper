#include <stdio.h>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <string.h>

#define si() (scanf("%d", &SCAN_INT), SCAN_INT)
#define MAXN 200005
int SCAN_INT;

typedef struct {
	int st, ed;
	int value;
} Edge;

int parent[20000];
int width[20000];
int level[20000];

Edge edge[1000000];
int n, m;

void solve() {
	n = si(), m = si();
	for (int i = 0; i < m; i++) {
		edge[i] = { si(), si(), si() };
	}

	std::sort(edge, edge + m, [](Edge a, Edge b) {
		return a.value > b.value;
	});

	for (int i = 1; i <= n; i++) {
		level[i] = 0;
		parent[i] = -1;
	}

	for (int i = 0; i < m; i++) {
		int h1 = edge[i].st, h2 = edge[i].ed;

		while (parent[h1] > 0) {
			h1 = parent[h1];
		}
		while (parent[h2] > 0) {
			h2 = parent[h2];
		}
		if (h1 == h2) continue;

		if (level[h1] > level[h2]) {
			parent[h2] = h1;
			width[h2] = edge[i].value;
		}
		else if (level[h1] < level[h2]) {
			parent[h1] = h2;
			width[h1] = edge[i].value;
		}
		else {
			parent[h1] = h2;
			level[h2]++;
			width[h1] = edge[i].value;
		}
	}

	for (int i = 1; i <= n; i++) {
		level[i] = 0;
	}

	for (int i = 1; i <= n; i++) {
		int h = i;
		while (parent[h] > 0) {
			h = parent[h];
		}
		level[h] = 1;
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (level[parent[j]] && !level[j]) {
				level[j] = level[parent[j]] + 1;
			}
		}
	}

	int q = si();
	long long int ans = 0;
	for (int i = 0; i < q; i++) {
		int a = si(), b = si();
		if (a == b) continue;
		int cw = 0x7fffffff;
		while (level[a] > level[b]) {
			cw = std::min(cw, width[a]);
			a = parent[a];
		}
		while (level[a] < level[b]) {
			cw = std::min(cw, width[b]);
			b = parent[b];
		}

		while (a != b) {
			cw = std::min(cw, width[a]);
			cw = std::min(cw, width[b]);
			a = parent[a];
			b = parent[b];
		}

		if (a < 0 || a == 0) {
			printf("ERROR\n");
			return;
		}

		ans += cw;
		//printf(": %d\n", cw);
	}

	printf("%lld\n", ans);
}
/*
int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	si();

	int n = si(), m = si();

	for (int i = 0; i < m; i++) {
		si(), si(), si();
	}
	int q = si();
	for (int i = 0; i < q; i++) {
		si(), si();
	}


	n = si(), m = si(); printf("%d %d\n", n, m);

	for (int i = 0; i < m; i++) {
		printf("%d ", si());
		printf("%d ", si());
		printf("%d\n", si());
	}
	q = si(); printf("%d\n", q);
	for (int i = 0; i < q; i++) {
		printf("%d ", si());
		printf("%d\n", si());
	}
	return 0;
}*/


int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (int t = si(); t--; ) solve();
}


