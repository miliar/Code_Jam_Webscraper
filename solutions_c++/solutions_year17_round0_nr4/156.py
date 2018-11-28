#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

typedef int flow_t;
const int MAXA = 105;
const int MAXN = MAXA * 6, MAXM = MAXA * MAXA * 2 + MAXA * 6, DIRECTED = 0, UNDIRECTED = 1;
const flow_t INFTY = 0x3fffffff;
enum {HORI, VERT, DIAG, DIAG2};
enum {NOT_HORI_VERT = 1, NOT_DIAG = 2, NO_INFO = 0};
int N, S, T, now;
int A, M, ans0;
char stage[MAXA][MAXA], stage2[MAXA][MAXA];
bool occupiedVert[MAXA], occupiedHori[MAXA], occupiedDiag[MAXA * 2], occupiedDiag2[MAXA * 2];

struct edge {
	flow_t remain;
	int endVertexId, nextEdgeId;
	int x, y, infoType;
}e[MAXM << 1];
struct vertex {
	int firstEdgeId, level, firstUnsaturEdgeId;
}v[MAXN];

void _addEdge(int begin, int end, flow_t c, int x = -1, int y = -1, int infoType = NO_INFO) {
	e[now].remain = c;
	e[now].endVertexId = end;
	e[now].nextEdgeId = v[begin].firstEdgeId;
	e[now].x = x;
	e[now].y = y;
	e[now].infoType = infoType;
	v[begin].firstEdgeId = now++;
}

void addEdge(int begin, int end, flow_t c, int edgeType, int x, int y, int infoType) {
	_addEdge(begin, end, c, x, y, infoType);
	_addEdge(end, begin, edgeType * c);
}

void init() {
	now = 0;
	for (int i = 0; i < N; ++i) v[i].firstEdgeId = -1;
}

bool markLevel(){
	for (int i = 0; i < N; ++i)
		v[i].level = -1, v[i].firstUnsaturEdgeId = v[i].firstEdgeId;
	v[S].level = 0;
	queue<int> Q;
	Q.push(S);
	while (!Q.empty()) {
		int x = Q.front();
		Q.pop();
		for (int i = v[x].firstEdgeId; i >= 0; i = e[i].nextEdgeId)
			if (e[i].remain && v[e[i].endVertexId].level < 0)
					v[e[i].endVertexId].level = v[x].level + 1, Q.push(e[i].endVertexId);
	}
	return v[T].level > 0;
}

flow_t extendFlow(int x, flow_t flow) {
	if (x == T) return flow;
	flow_t t, total = 0;
	for (int &i = v[x].firstUnsaturEdgeId; i >= 0; i = e[i].nextEdgeId) {
		if (v[e[i].endVertexId].level == v[x].level + 1 && e[i].remain) {
			if (t = extendFlow(e[i].endVertexId, min(flow, e[i].remain)))
				e[i].remain -= t, e[i ^ 1].remain += t, flow -= t, total += t;
			if (0 == flow) break;
		}
	}
	return total;
}

flow_t Dinic() {
	flow_t flow, total = 0;
	while (markLevel())
		while (flow = extendFlow(S, INFTY))
			total += flow;
	return total;
}

inline int transform(int type, int x) {
	switch(type) {
		case VERT: return x;
		case HORI: return x + A;
		case DIAG: return x + A * 2;
		case DIAG2: return x + A - 1 + A * 4 - 1;
	}
}

void buildGraph() {
	N = A * 6, S = N - 2, T = N - 1;
	init();
	for (int i = 0; i < A; ++i)
		if (!occupiedVert[i])
			addEdge(S, transform(VERT, i), 1, DIRECTED, 0, 0, NO_INFO);
	for (int i = 0; i < A; ++i)
		if (!occupiedHori[i])
			addEdge(transform(HORI, i), T, 1, DIRECTED, 0, 0, NO_INFO);
	for (int i = 0; i <= A * 2 - 2; ++i)
		if (!occupiedDiag[i])
			addEdge(S, transform(DIAG, i), 1, DIRECTED, 0, 0, NO_INFO);
	for (int i = 1 - A; i <= A - 1; ++i)
		if (!occupiedDiag2[i + A - 1])
			addEdge(transform(DIAG2, i), T, 1, DIRECTED, 0, 0, NO_INFO);
	for (int i = 0; i < A; ++i) {
		for (int j = 0; j < A; ++j) {
			addEdge(transform(VERT, i), transform(HORI, j), 1, DIRECTED, i, j, NOT_HORI_VERT);
			addEdge(transform(DIAG, i + j), transform(DIAG2, i - j), 1, DIRECTED, i, j, NOT_DIAG);
		}
	}
}

void printStage() { // Reconstruct the stage from the network
	for (int i = 0; i < A; ++i)
		for (int j = 0; j < A; ++j)
			stage2[i][j] = stage[i][j];
	for (int i = 0; i < now; ++i) {
		if (NO_INFO != e[i].infoType && 0 == e[i].remain)
			stage2[e[i].x][e[i].y] |= e[i].infoType;
	}
	int nChange = 0;
	for (int i = 0; i < A; ++i)
		for (int j = 0; j < A; ++j)
			if (stage2[i][j] != stage[i][j])
				++nChange;
	printf("%d\n", nChange);
	for (int i = 0; i < A; ++i)
		for (int j = 0; j < A; ++j)
			if (stage2[i][j] != stage[i][j])
				printf("%c %d %d\n", stage2[i][j] == 3 ? 'o' : ((stage2[i][j] & NOT_HORI_VERT) ? 'x' : '+'), i + 1, j + 1);
}

int main() {
	int nCase, x, y;
	char c;
	scanf("%d", &nCase);
	for (int t = 1; t <= nCase; ++t) {
		scanf("%d%d", &A, &M);
		memset(stage, 0, sizeof(stage));
		memset(occupiedVert, 0, sizeof(occupiedVert));
		memset(occupiedHori, 0, sizeof(occupiedHori));
		memset(occupiedDiag, 0, sizeof(occupiedDiag));
		memset(occupiedDiag2, 0, sizeof(occupiedDiag2));
		ans0 = 0;
		for (int i = 0; i < M; ++i) {
			scanf(" %c%d%d", &c, &x, &y);
			--x, --y;
			if (c != '+') {
				stage[x][y] |= NOT_HORI_VERT, ++ans0;
				occupiedVert[x] = true;
				occupiedHori[y] = true;
			}
			if (c != 'x') {
				stage[x][y] |= NOT_DIAG, ++ans0;
				occupiedDiag[x + y] = true;
				occupiedDiag2[x - y + A - 1] = true;
			}
		}
		buildGraph();
		flow_t ans = Dinic();
		printf("Case #%d: %d ", t, ans0 + ans);
		printStage();
	}
	return 0;
}
