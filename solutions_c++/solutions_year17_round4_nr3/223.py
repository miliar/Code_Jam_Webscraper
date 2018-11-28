#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
const int MAX = 55, MAX_ID = 2600;

enum DIRECTION {
	UP, RIGHT, DOWN, LEFT
};

struct traveling {
	DIRECTION dir;
	int y, x;
};

// | true(positive)
// - false(negative)
int maxId;
struct result {
	int id;  // -1 or beam ID
	bool side;

	result inv() {
		return { id, !side };
	}

	int cellId() {
		return side ? id : id + maxId;
	}
};

// input
int w, h, id[MAX][MAX];
char map[MAX][MAX];

// travel related
bool visited[MAX][MAX][4];
result resultMemo[MAX][MAX][4];

// SCC related
vector < int > e[MAX_ID*2];

int stack[MAX_ID*2], top, sid[MAX_ID*2], currentId, groupId[MAX_ID*2];
vector < vector < int > > sccGroup;

void init() {
	maxId = 0;
	for (int y = 0; y < MAX; y++) {
		for (int x = 0; x < MAX; x++) {
			id[y][x] = -1;
			for (int t = 0; t < 4; t++) {
				visited[y][x][t] = 0;
			}
		}
	}

	top = 0;
	currentId = 0;
	for (int i = 0; i < MAX_ID*2; i++) {
		e[i].clear();
		sid[i] = 0;
		groupId[i] = 0;
	}

	sccGroup.clear();
}

void input() {
	scanf("%d%d", &h, &w);

	for (int y = 1; y <= h; y++) {
		for (int x = 1; x <= w; x++) {
			char c[2];
			scanf("%1s", c);
			map[y][x] = c[0];

			if (map[y][x] == '-' || map[y][x] == '|') {
				id[y][x] = ++maxId;
			}
		}
	}
}

int to[4][2] = {
	-1, 0, 0, 1, 1, 0, 0, -1
};

result travel(traveling &now) {
	result &resultCell = resultMemo[now.y][now.x][now.dir];
	if (visited[now.y][now.x][now.dir]) {
		return resultCell;
	}

	visited[now.y][now.x][now.dir] = 1;

	now.y += to[now.dir][0];
	now.x += to[now.dir][1];

	if (now.x < 1 || now.x > w || now.y < 1 || now.y > h || map[now.y][now.x] == '#') {
		resultCell = { -1, false };
	} else if (map[now.y][now.x] == '-' || map[now.y][now.x] == '|') {
		resultCell = { id[now.y][now.x], now.dir == UP || now.dir == DOWN };
	} else {
		if (map[now.y][now.x] == '/') {
			switch (now.dir) {
				case UP:
					now.dir = RIGHT;
					break;
				case RIGHT:
					now.dir = UP;
					break;
				case DOWN:
					now.dir = LEFT;
					break;
				case LEFT:
					now.dir = DOWN;
					break;
			}
		} else if (map[now.y][now.x] == '\\') {
			switch (now.dir) {
				case UP:
					now.dir = LEFT;
					break;
				case RIGHT:
					now.dir = DOWN;
					break;
				case DOWN:
					now.dir = RIGHT;
					break;
				case LEFT:
					now.dir = UP;
					break;
			}
		}
		resultCell = travel(now);
	}

	return resultCell;
}

int traverse(int node) {
	sid[node] = ++currentId;
	stack[top++] = node;

	int lowlink = sid[node];
	for (auto next : e[node]) {
		if (sid[next] == 0) {
			lowlink = min(lowlink, traverse(next));
		} else if (groupId[next] == 0) {
			lowlink = min(lowlink, sid[next]);
		}
	}

	if (lowlink == sid[node]) {
		sccGroup.push_back(vector < int >());
		while (1) {
			int now = stack[top-1];
			top--;

			groupId[now] = sccGroup.size();
			sccGroup[groupId[now]-1].push_back(now);

			if (now == node) break;
		}
	}

	return lowlink;
}

bool scc() {
	for (int v = 1; v <= 2*maxId; v++) {
		if (sid[v] == 0) {
			traverse(v);
		}
	}

	for (int v = 1; v <= maxId; v++) {
		if (groupId[v] == groupId[v+maxId]) {
			return false;
		}
	}

	return true;
}

void addOr(result r1, result r2) {
	e[r1.inv().cellId()].push_back(r2.cellId());
	e[r2.inv().cellId()].push_back(r1.cellId());
}

bool solve() {
	for (int y = 1; y <= h; y++) {
		for (int x = 1; x <= w; x++) {
			if (map[y][x] == '.') {
				result up, right, down, left;

				traveling now;
				now = { UP, y, x };
				up = travel(now);
				now = { RIGHT, y, x };
				right = travel(now);
				now = { DOWN, y, x };
				down = travel(now);
				now = { LEFT, y, x };
				left = travel(now);

				int hor = (left.id != -1) + (right.id != -1);
				int ver = (up.id != -1) + (down.id != -1);

				if (hor%2 == 0 && ver%2 == 0) {
					return false;
				} else if (hor%2 == 0) {
					// only vertical
					if (up.id != -1) {
						addOr(up, up);
					} else {
						addOr(down, down);
					}
				} else if (ver%2 == 0) {
					// only horizontal
					if (left.id != -1) {
						addOr(left, left);
					} else {
						addOr(right, right);
					}
				} else {
					// both
					result horResult, verResult;
					horResult = left.id != -1 ? left : right;
					verResult = up.id != -1 ? up : down;
					addOr(horResult, verResult);
				}
			}
		}
	}

	for (int y = 1; y <= h; y++) {
		for (int x = 1; x <= w; x++) {
			if (map[y][x] == '-' || map[y][x] == '|') {
				result up, right, down, left;

				traveling now;
				now = { UP, y, x };
				up = travel(now);
				now = { RIGHT, y, x };
				right = travel(now);
				now = { DOWN, y, x };
				down = travel(now);
				now = { LEFT, y, x };
				left = travel(now);

				int nowId = id[y][x];
				if (up.id != -1 || down.id != -1) {
					addOr({ nowId, false }, { nowId, false });
				}
				if (left.id != -1 || right.id != -1) {
					addOr({ nowId, true }, { nowId, true });
				}
			}
		}
	}

	return scc();
}

void printAnswer() {
	for (int y = 1; y <= h; y++) {
		for (int x = 1; x <= w; x++) {
			if (map[y][x] == '-' || map[y][x] == '|') {
				int nowId = id[y][x];
				putchar(groupId[nowId] < groupId[nowId+maxId] ? '|' : '-');
			} else {
				putchar(map[y][x]);
			}
		}
		puts("");
	}
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for (int nowCase = 1; nowCase <= numCase; nowCase++) {
		init();
		input();

		printf("Case #%d: ", nowCase);
		if (solve()) {
			puts("POSSIBLE");
			printAnswer();
		} else {
			puts("IMPOSSIBLE");
		}
	}

	return 0;
}