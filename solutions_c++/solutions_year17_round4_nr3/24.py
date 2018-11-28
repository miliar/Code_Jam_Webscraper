#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <iomanip>
#include <string>
#include <sstream>
#include <cmath>
#include <cassert>
#include <cstring>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int MAXV = 20000;
vector<int> xx[2*MAXV], *e = xx+MAXV;
bool assign[MAXV];

void reset() { for (auto& x: xx) x.clear(); }

void edge(int x, int y) { e[x].push_back(y); }
#define vee(a,b) (edge(~(a),b), edge(~(b),a))
#define implies(a,b) (edge(a,b), edge(~(b),~(a)))
#define eq(a,b) (implies(a,b), implies(b,a))
#define tru(a) (edge(~(a),a))

vector<int> S, B;
int xI[2*MAXV], *I = xI+MAXV, C;
bool scc(int v) {
  S.push_back(v);
  B.push_back(I[v] = S.size());
  for (int w: e[v]) if (I[w]) {
    while (I[w] < B.back()) B.pop_back();
  } else if (!scc(w)) return false;
  if (I[v] == B.back()) {
    for (B.pop_back(), ++C; I[v] <= S.size(); S.pop_back()) {
      int w = S.back();
      if (I[~w] == C) return false;
      if (I[~w] < MAXV) assign[w<0?~w:w] = w>=0;
      I[w] = C;
    }
  }
  return true;
}

bool go(int n) {
  S.clear(); B.clear();
  memset(xI, 0, sizeof(xI));
  memset(assign, 0, sizeof(assign));
  C = MAXV;
  for (int i = -n; i < n; ++i) if (!I[i] && !scc(i)) return false;
  return true;
}

int xdir[4] = {1,-1,0,0};
int ydir[4] = {0,0,1,-1};

int main() {
    int T;
    cin >> T;
    for (int caseno = 1; caseno <= T; ++caseno) {
        reset();
        int r, c;
        cin >> r >> c;
        vector<string> M(r);
        for (int i = 0; i < r; ++i) cin >> M[i];
#define P(x,y) ((x)+(y)*c)
        for (int y = 0; y < r; ++y) {
            for (int x =0 ; x < c; ++x) {
                if (M[y][x] != '.' && M[y][x] != '|' && M[y][x] != '-') continue;
                int hits[4] = {-1,-1,-1,-1};
                int orient[4] = {};
                for (int d = 0; d < 4; ++d) {
                    int dx = xdir[d];
                    int dy = ydir[d];
                    int cx = x, cy = y;
                    while (1) {
                        cx += dx;
                        cy += dy;
                        if (cx < 0 || cx >= c || cy < 0 || cy >= r) break;
                        if (M[cy][cx] == '#') {
                            break;
                        } else if (M[cy][cx] == '/') {
                            if (dx) {
                                dy = -dx;
                                dx = 0;
                            } else {
                                dx = -dy;
                                dy = 0;
                            }
                        } else if (M[cy][cx] == '\\') {
                            if (dx) {
                                dy = dx;
                                dx = 0;
                            } else {
                                dx = dy;
                                dy = 0;
                            }
                        } else if (M[cy][cx] == '|' || M[cy][cx] == '-') {
                            hits[d] = P(cx, cy);
                            if ((M[cy][cx] == '-') == (dx != 0)) {
                                orient[d] = 1;
                            } else {
                                orient[d] = 0;
                            }
                            break;
                        }
                    }
                }
                if (hits[0] >= 0 && hits[1] >= 0) {
                    tru(orient[0] ? hits[0] : ~hits[0]);
                    tru(orient[1] ? hits[1] : ~hits[1]);
                    hits[0] = -1;
                    hits[1] = -1;
                }
                if (hits[2] >= 0 && hits[3] >= 0) {
                    tru(orient[2] ? hits[2] : ~hits[2]);
                    tru(orient[3] ? hits[3] : ~hits[3]);
                    hits[2] = -1;
                    hits[3] = -1;
                }
                int ok = 0;
                for (int d=  0; d < 4; ++d) ok += (hits[d] >= 0);
                if (M[y][x] == '.') {
                if (ok == 0) {
                    goto impossible;
                }
                if (ok == 1) {
                    for (int d = 0; d < 4; ++d) if (hits[d] >= 0) {
                            tru(orient[d] ? ~hits[d] : hits[d]);
                        }
                }
                if (ok == 2) {
                    int d = 0;
                    int a, b;
                    for (; d < 4; ++d) if (hits[d] >= 0) {
                            a = (orient[d] ? ~hits[d] : hits[d]);
                            break;
                        }
                    for (++d; d < 4; ++d) if (hits[d] >= 0) {
                            b = (orient[d] ? ~hits[d] : hits[d]);
                            break;
                        }
                    vee(a, b);
                }
                } else {
                    for (int d = 0; d < 4; ++d) if (hits[d] >= 0) {
                            tru(orient[d] ? hits[d] : ~hits[d]);
                        }
                }
            }
        }
        if (!go(r * c)) goto impossible;
        printf("Case #%d: POSSIBLE\n", caseno);
        for (int y = 0; y < r; ++y) {
            for (int x = 0; x < c; ++x) {
                if (M[y][x] == '|' && assign[P(x, y)]) cout << '-';
                else if (M[y][x] == '-' && assign[P(x, y)]) cout << '|';
                else cout << M[y][x];
            }
            cout << endl;
        }
        continue;
    impossible:
        printf("Case #%d: IMPOSSIBLE\n", caseno);
    }
}
