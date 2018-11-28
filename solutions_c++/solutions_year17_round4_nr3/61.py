#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
#define all(x) (x).begin(), (x).end()

void read();
void kill();

const int R = 53;
const int M = 207;

int r, c;
int n;
char a[R][R];
int u[R][R];
int id[R][R];
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
bool bad;
vector<int> cur;
vector<int> g[M], gt[M];

#define DOWN 0
#define RIGHT 1
#define UP 2
#define LEFT 3

void read() {
  cin >> r >> c;
  for (int i = 0; i < r; ++i)
    for (int j = 0; j < c; ++j)
        cin >> a[i][j];
}

bool isBeam(int x, int y) {
  return a[x][y] == '-' || a[x][y] == '|';
}

bool isMirror(int x, int y) {
  return a[x][y] == '/' || a[x][y] == '\\';
}

int rot(int dir, char c) {
  map<int, int> back;
  back[UP] = LEFT;
  back[LEFT] = UP;
  back[DOWN] = RIGHT;
  back[RIGHT] = DOWN;
  if (c == '\\') {
    return back[dir];
  }

  map<int, int> slash;
  slash[UP] = RIGHT;
  slash[RIGHT] = UP;
  slash[DOWN] = LEFT;
  slash[LEFT] = DOWN;
  return slash[dir];
}

bool inside(int x, int y) {
  return 0 <= x && x < r && 0 <= y && y < c;
}

void findWay(int x, int y, int dir) {
  if (!inside(x, y))
    return;

  if (u[x][y] >= 5) {
    bad = true;
    return;
  }

  u[x][y]++;

  if (isBeam(x, y))
    cur.push_back(2 * id[x][y] + (dir % 2));
  
  if (a[x][y] == '#')
    return;

  if (isMirror(x, y))
    dir = rot(dir, a[x][y]);

  findWay(x + dx[dir], y + dy[dir], dir);
}

int vertway(int x, int y, int dir) {
  for (int i = 0; i < r; ++i)
    for (int j = 0; j < c; ++j)
      u[i][j] = false;

  bad = false;
  cur.clear();

  findWay(x + dx[dir], y + dy[dir], dir);
  findWay(x - dx[dir], y - dy[dir], (dir + 2) % 4);

  if (cur.size() == 1u) 
    return cur[0];
  if (cur.empty())
    return -2;
  
  return -1;
}

void addEdge(int u, int v) {
  g[u].push_back(v);
  gt[v].push_back(u);
}

void add(int u, int v) {
  if (u < 0)
    u = v;
  if (v < 0)
    v = u;
  //cerr << " add " << u << " " << v << endl;

  addEdge(u ^ 1, v);
  addEdge(v ^ 1, u);
}

vector<bool> used;
vector<int> order, comp;

void dfs1(int v) {
	used[v] = true;
	for (size_t i = 0; i < g[v].size(); ++i) {
		int to = g[v][i];
		if (!used[to])
			dfs1(to);
	}
	order.push_back(v);
}

void dfs2(int v, int cl) {
	comp[v] = cl;
	for (size_t i = 0; i < gt[v].size(); ++i) {
		int to = gt[v][i];
		if (comp[to] == -1)
			dfs2(to, cl);
	}
}

map<int, char> res;

bool sat2() {
  order.clear();
  int N = 2 * n;

  used.assign(N, false);
	for (int i = 0; i < N; ++i)
		if (!used[i])
			dfs1(i);

	comp.assign(N, -1);
	for (int i = 0, j = 0; i < N; ++i) {
		int v = order[N - i - 1];
		if (comp[v] == -1)
			dfs2(v, j++);
	}

  //for (int i = 0; i < N; ++i)
    //cerr << comp[i] << " ";
  //cerr << endl;

	for (int i = 0; i < N; ++i)
		if (comp[i] == comp[i ^ 1]) {
			return false;
		}
  
	for (int i = 0; i < n; ++i) {
		res[i] = comp[2 * i] > comp[2 * i + 1] ? '|' : '-';
	}
  return true;
}

void kill() {
  n = 0;
  for (int x = 0; x < r; ++x)
    for (int y = 0; y < c; ++y)
      if (isBeam(x, y)) {
        id[x][y] = n++;
      } else {
        id[x][y] = -1;
      }

  for (int i = 0; i < 2 * n; ++i) {
    g[i].clear();
    gt[i].clear();
  }

  for (int x = 0; x < r; ++x)
    for (int y = 0; y < c; ++y) {
      if (a[x][y] == '.') {
        int id1 = vertway(x, y, UP);
        int id2 = vertway(x, y, LEFT);
        if (id1 < 0 && id2 < 0) {
          cout << "IMPOSSIBLE\n";
          return;
        }
        add(id1, id2);
      }
      if (isBeam(x, y)) {
        int cur = id[x][y];
        if (vertway(x, y, UP) != -2) {
          add(2 * cur + 1, 2 * cur + 1);
        }
        if (vertway(x, y, LEFT) != -2) {
          add(2 * cur, 2 * cur);
        }
      }
    }

  if (!sat2()) {
    cout << "IMPOSSIBLE\n";
    return;
  }

  cout << "POSSIBLE\n";
  for (int i = 0; i < r; ++i, cout << "\n")
    for (int j = 0; j < c; ++j) {
      if (isBeam(i, j))
        cout << res[id[i][j]];
      else
        cout << a[i][j];
    }
}


int main() {
#ifdef LOCAL
  //assert(freopen("c.in", "r", stdin));
#endif
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
