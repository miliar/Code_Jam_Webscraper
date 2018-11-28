#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

const string PROGRAM_NAME = "google";

vector<int> tarjan(const vector<vector<int> >& ne) {
  int n = (int)ne.size();
  int number = 0;
  vector<pair<int, int> > st(n * 2);
  vector<int> st2(n * 2);
  int size, sizeOfStack;
  vector<vector<int> > rev(n);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < (int)ne[i].size(); j++)
      rev[ne[i][j]].push_back(i);
  vector<int> komp(n, -1);
  pair<int, int> cur;
  for (int i = 0; i < n; i++) {
    if (komp[i] >= 0)
      continue;
    vector<bool> in_komp(n);
    size = sizeOfStack = 0;
    st[size++] = make_pair(i, 0);
    in_komp[i] = true;
    while (size) {
      cur = st[size - 1];
      if (cur.second == (int)ne[cur.first].size()) {
        st2[sizeOfStack++] = cur.first;
        size--;
      } else if (komp[ne[cur.first][cur.second]] == -1
          && !in_komp[ne[cur.first][cur.second]]) {
        in_komp[ne[cur.first][cur.second]] = true;
        st[size - 1].second++;
        st[size++] = make_pair(ne[cur.first][cur.second], 0);
      } else
        st[size - 1].second++;
    }
    for (int j = sizeOfStack - 1; j >= 0; j--) {
      if (komp[st2[j]] >= 0)
        continue;
      queue<int> tc;
      komp[st2[j]] = number++;
      tc.push(st2[j]);
      while (!tc.empty()) {
        int c = tc.front();
        tc.pop();
        for (int k = 0; k < (int)rev[c].size(); k++)
          if (komp[rev[c][k]] == -1 && in_komp[rev[c][k]]) {
            komp[rev[c][k]] = komp[st2[j]];
            tc.push(rev[c][k]);
          }
      }
    }
  }
  return komp;
}

void condense(const vector<vector<int> >& ne, const vector<int>& komp,
    const vector<vector<int> >& komp_vertices, vector<vector<int> >& res) {

  int komp_num = (int)komp_vertices.size();
  res.clear();
  res.resize(komp_num);
  vector<char> reachable(komp_num, 0);
  for (int i = 0; i < komp_num; ++i) {
    fill(all(reachable), 0);

    for (int j = 0; j < (int)komp_vertices[i].size(); ++j) {
      int ver = komp_vertices[i][j];
      for (int l = 0; l < (int)ne[ver].size(); ++l) {
        if (komp[ne[ver][l]] != komp[ver]) {
          if (reachable[komp[ne[ver][l]]] == 0) {
            reachable[komp[ne[ver][l]]] = 1;
            res[komp[ver]].push_back(komp[ne[ver][l]]);
          }
        }
      }
    }
  }
}

inline int get_negation(int index, int n) {
  return 2 * n + 2 - index;
}

/**
 * @param n - number of vertices
 * @param rels - set of pairs of the type (node_i, node_j) where both are 1
 *     indexed.
 * @return empty vector if no valid assignment can be found and some valid
 *     assignment if there is one.
 */
vector<char> twoSat(int n, vector<pair<int, int> > rels) {
  vector<vector<int> > ne(2 * n + 2);
  for (int i = 0; i < (int)rels.size(); i++) {
    ne[n + 1 - rels[i].first].push_back(n + 1 + rels[i].second);
    ne[n + 1 - rels[i].second].push_back(n + 1 + rels[i].first);
  }
  vector<int> komp = tarjan(ne);
  for (int i = 1; i <= n; i++) {
    if (komp[n + 1 - i] == komp[n + 1 + i]) {
      return vector<char>();
    }
  }

  int komp_num = *max_element(all(komp)) + 1;
  vector<vector<int> > komp_vertices(komp_num);
  for (int i = 1; i <= n; ++i) {
    komp_vertices[komp[n + 1 + i]].push_back(n + 1 + i);
    komp_vertices[komp[n + 1 - i]].push_back(n + 1 - i);
  }

  vector<vector<int> > komp_ne;
  condense(ne, komp, komp_vertices, komp_ne);
  int m = komp_ne.size();
  vector<int> dads(m, 0);
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < (int)komp_ne[i].size(); ++j) {
      dads[komp_ne[i][j]]++;
    }
  }
  queue<int> orphans;
  for (int i = 0; i < (int)dads.size(); ++i) {
    if (dads[i] == 0) {
      orphans.push(i);
    }
  }

  vector<char> vis(m, 0);
  const char notasigned = 2;
  vector<char> truth(m, notasigned);

  vector<char> processed(m, 0);
  while (!orphans.empty()) {
    int cur = orphans.front();
    orphans.pop();
    if (truth[cur] != notasigned) {
      continue;
    }

    queue<int> tc;
    truth[cur] = 0;
    tc.push(cur);

    while (!tc.empty()) {
      int c = tc.front();
      tc.pop();

      for (int i = 0; i < (int)komp_ne[c].size(); ++i) {
        dads[komp_ne[c][i]]--;
        if (dads[komp_ne[c][i]] == 0) {
          orphans.push(komp_ne[c][i]);
        }
      }

      for (int j = 0; j < (int)komp_vertices[c].size(); ++j) {
        int cnode = komp_vertices[c][j];
        int ckomp = komp[get_negation(cnode, n)];

        if (truth[ckomp] == notasigned) {
          truth[ckomp] = 1 - truth[c];
          tc.push(ckomp);
        }
      }
    }
  }
  vector<char> solution(n + 1);
  for (int i = 1; i <= n; ++i) {
    solution[i] = truth[komp[n + 1 + i]];
  }
  return solution;
}

int r, c;


char vis[51][51][4];
int moves[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};


int bounce(char mirror, int d) {
  if (mirror == '/') {
    switch (d) {
    case 0:
      return 1;
    case 1:
      return 0;
    case 2:
      return 3;
    case 3:
      return 2;
    default:
      throw "Wrong d /";
    }
  } else if (mirror == '\\') {
    switch (d) {
    case 0:
      return 3;
    case 1:
      return 2;
    case 2:
      return 1;
    case 3:
      return 0;
    default:
      throw "Wrong d \\";
    }
  } else {
    return d;
  }
}

struct pos {
  int x, y;
  int d;
  pos(int _x = 0, int _y = 0, int _d = 0)
      : x(_x), y(_y), d(_d) {
  }
};

struct parent {
  int x, y;
  bool turned;
};

vector<pair<int, int> > free_cells;
vector<vector<vector<parent> > > parents;
bool check(int x, int y, bool turned, const vector<string>& map_given) {
  memset(vis, 0, sizeof(vis));

  queue<pos> q;

  char c1;
  if (!turned) {
    c1 = map_given[x][y];
  } else {
    c1 = map_given[x][y] == '|' ? '-' : '|';
  }
  if (c1 == '-') {
    vis[x][y][1] = vis[x][y][3] = 1;
    q.push(pos(x, y, 1));
    q.push(pos(x, y, 3));
  } else {
    vis[x][y][2] = vis[x][y][0] = 1;
    q.push(pos(x, y, 2));
    q.push(pos(x, y, 0));
  }
  while (!q.empty()) {
    pos cur = q.front();
    q.pop();
    int tx = cur.x + moves[cur.d][0];
    int ty = cur.y + moves[cur.d][1];
    if (tx >= r || tx < 0 || ty >= c || ty < 0 || map_given[tx][ty] == '#') {
      continue;
    } else if (map_given[tx][ty] == '-' || map_given[tx][ty] == '|') {
      return false;
    } else if (map_given[tx][ty] == '.') {
      if (vis[tx][ty][cur.d] == 0) {
        vis[tx][ty][cur.d] = 1;
        q.push(pos(tx, ty, cur.d));
      }
    } else {  // mirror
      int nd = bounce(map_given[tx][ty], cur.d);
      if (vis[tx][ty][nd] == 0) {
        vis[tx][ty][nd] = 1;
        q.push(pos(tx, ty, nd));
      }
    }
  }

  for (int i = 0; i < (int)free_cells.size(); ++i) {
    for (int l = 0; l < 4; ++l) {
      if (vis[free_cells[i].first][free_cells[i].second][l]) {
        parent temp;
        temp.x = x;
        temp.y = y;
        temp.turned = turned;
        parents[free_cells[i].first][free_cells[i].second].push_back(temp);
        break;
      }
    }
  }
  return true;
}

int mapping[52][52], mapping_size = 0;

pair<bool, int> get_index(const parent& p) {
  int index = mapping[p.x][p.y];
  bool good = index != -1;
  if (p.turned) {
    index = -index;
  }
  return mpair(good, index);
}

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    cerr << "Processing case " << it << endl;

    cin >> r >> c;
    vector<string> map_given(r);
    getline(cin, map_given[0]);
    for (int i = 0; i < (int)map_given.size(); ++i) {
      getline(cin, map_given[i]);
    }
    mapping_size = 0;
    memset(mapping, -1, sizeof(mapping));
    parents.clear();
    parents.resize(r, vector<vector<parent> >(c, vector<parent>()));
    free_cells.clear();
    for (int x = 0; x < r; ++x) {
      for (int y = 0; y < c; ++y) {
        if (map_given[x][y] == '.') {
          free_cells.push_back(mpair(x, y));
        }
      }
    }
    bool possible = true;
    vector<pair<int, int> > unk;
    for (int x = 0; x < r && possible; ++x) {
      for (int y = 0; y < c && possible; ++y) {
        if (map_given[x][y] == '|' || map_given[x][y] == '-') {
          bool c1 = check(x, y, false, map_given);
          bool c2 = check(x, y, true, map_given);
          if (!c1 && !c2) {
            possible = false;
            break;
          } else if (c1 && c2) {
            mapping_size++;
            mapping[x][y] = mapping_size;
            unk.push_back(mpair(x, y));
          } else if (c2) {
            map_given[x][y] = (map_given[x][y] == '|' ? '-' : '|');
          }
        }
      }
    }
    vector<pair<int, int> > rels;
    for (int i = 0; i < (int)free_cells.size(); ++i) {
      int x = free_cells[i].first;
      int y = free_cells[i].second;
      if (parents[x][y].size() == 0) {
        possible = false;
        break;
      }
      if (parents[x][y].size() == 1) {
        pair<bool, int> index = get_index(parents[x][y][0]);
        if (index.first) {
          rels.push_back(mpair(index.second, index.second));
        }
      } else if (parents[x][y].size() == 2) {
        pair<bool, int> index1 = get_index(parents[x][y][0]);
        pair<bool, int> index2 = get_index(parents[x][y][1]);
        if (index1.first && index2.first) {
          rels.push_back(mpair(index1.second, index2.second));
        }
      }
    }
    vector<char> solution = twoSat((int)unk.size(), rels);
    if (solution.size() == 0) {
      possible = false;
    }
    string res;
    if (possible) {
      res = "POSSIBLE";
    } else {
      res = "IMPOSSIBLE";
    }
    cout << "Case #" << it << ": " << res << endl;
    if (possible) {
      for (int i = 0; i < (int)unk.size(); ++i) {
        int x = unk[i].first;
        int y = unk[i].second;
        if (!solution[i + 1]) {
          map_given[x][y] = (map_given[x][y] == '|' ? '-' : '|');
        }
      }
      for (int i = 0; i < (int)map_given.size(); ++i) {
        cout << map_given[i] << endl;
      }
    }
  }
  return 0;
}
