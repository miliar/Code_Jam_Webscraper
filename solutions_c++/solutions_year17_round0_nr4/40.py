#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

int N, M;

int ROWS, COLS, D1, D2, source, sink;
int adj[1000][1000];
int cap[1000][1000];
int degree[1000];

char old[1000][1000];


void add(int a, int b) {
	adj[a][degree[a]++] = b;
	adj[b][degree[b]++] = a;
	cap[a][b] = 1;
	cap[b][a] = 0;
}

void flow(int a, int b) {
	cap[a][b] = 0;
	cap[source][a] = 0;
	cap[b][sink] = 0;
}

int res;

void read() {


	scanf("%d%d", &N, &M);

	ROWS = 1;
	COLS = N + 1;
	D1 = 2 * N + 1;
	D2 = 4 * N;
	source = 0;
	sink = D2 + 2 * N;
	memset(degree, 0, sizeof(degree));
	memset(old, '.', sizeof(old));

	for (int i = 0; i < N; i++) {
		add(source, ROWS + i);
		add(COLS + i, sink);
		for (int j = 0; j < N; j++) {
			add(ROWS + i, COLS + j);
			add(D1 + i + j, D2 + i - j + N - 1);
		}
	}

	for (int i = 0; i < 2 * N - 1; i++) {
		add(source, D1 + i);
		add(D2 + i, sink);
	}
	res = 0;
	for (int i = 0; i < M; i++) {
		char s[5];
		int a, b;
		scanf("%s%d%d", s, &a, &b);
		a--;
		b--;
		old[a][b] = s[0];
		if (s[0] == 'x') {
			flow(ROWS + a, COLS + b);
			res++;
		} else if (s[0] == '+') {
			flow(D1 + a + b, D2 + a - b + N - 1);
			res++;
		} else {
			flow(ROWS + a, COLS + b);
			flow(D1 + a + b, D2 + a - b + N - 1);
			res += 2;
		}
	}

}

bool mark[1000];

bool dfs(int node) {
	if (node == sink) return true;
	mark[node] = true;
	for (int i = 0; i < degree[node]; i++) {
		int w = adj[node][i];
		if (!mark[w] && cap[node][w] > 0 && dfs(w)) {
			cap[node][w]--;
			cap[w][node]++;
			return true;
		}
	}
	return false;
}

void process() {
	memset(mark, false, sizeof(mark));
	while (dfs(source)) {
		memset(mark, false, sizeof(mark));
		res++;
	}
	vector<pair<char, pair<int,int> > > r;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int a = 0;
			int b = 0;
			if (cap[ROWS+i][COLS+j] == 0) {
				a++;
			}
			if (cap[D1 + i + j][D2 + i - j + N-1] == 0) {
				b++;
			}
			char c = '.';
			if (a && b) c = 'o';
			else if (a) c = 'x';
			else if (b) c = '+';

			if (c != old[i][j]) {
				r.push_back(make_pair(c, make_pair(i+1, j+1)));
			}
		}
	}
	printf("%d %d\n", res, (int) r.size());
	for (int i = 0; i < r.size(); i++) {
		printf("%c %d %d\n", r[i].first, r[i].second.first, r[i].second.second);
	}
}

int main() {

	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}