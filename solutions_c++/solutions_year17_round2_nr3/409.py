#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;

const int MAX = 110;
const ll INF = 1234567890123456;

struct horse {
	int maxDist, speed;
};

int n, numPair;
ll dist[MAX][MAX];
horse horses[MAX];

void input() {
	scanf("%d%d", &n, &numPair);

	for (int i = 0; i < n; i++) {
		scanf("%d%d", &horses[i].maxDist, &horses[i].speed);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%lld", &dist[i][j]);
			if (dist[i][j] == -1) dist[i][j] = INF;
		}
	}
}

double reach[MAX];
bool select[MAX];

double delivery(int from, int to) {
	for (int i = 0; i < n; i++) {
		reach[i] = INF;
		select[i] = 0;
	}
	reach[from] = 0;

	for (int i = 0; i < n; i++) {
		double min_reach = INF;
		int now = -1;
		for (int t = 0; t < n; t++) {
			if (reach[t] < min_reach && !select[t]) {
				min_reach = reach[t];
				now = t;
			}
		}
		for (int next = 0; next < n; next++) {
			if (dist[now][next] <= horses[now].maxDist && reach[next] > reach[now] + (double)dist[now][next]/horses[now].speed) {
				reach[next] = reach[now] + (double)dist[now][next]/horses[now].speed;
			}
		}
		select[now] = 1;
	}

	return reach[to];
}

void solve() {
	for (int i = 0; i < n; i++) {
		dist[i][i] = 0;
	}

	for (int middle = 0; middle < n; middle++) {
		for (int start = 0; start < n; start++) {
			for (int end = 0; end < n; end++) {
				if (dist[start][end] > dist[start][middle]+dist[middle][end]) {
					dist[start][end] = dist[start][middle]+dist[middle][end];
				}
			}
		}
	}

	for (int i = 0; i < numPair; i++) {
		int from, to;
		scanf("%d%d", &from, &to);
		from--;
		to--;
		printf(" %.10lf", delivery(from, to));
	}
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for (int nowCase = 1; nowCase <= numCase; nowCase++) {
		input();

		printf("Case #%d:", nowCase);
		solve();
		puts("");
	}

	return 0;
}