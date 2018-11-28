#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int X, Y;
vector<string> G;
vector<int> bx, by;
int hv[100][100], vv[100][100], hvh[100][100], vvh[100][100];

bool doit(int x, int y, int dx, int dy, bool fill, int h = 0, int i = 0) {
//cout << "doit " << x << ',' << y << " " << dx << ',' << dy << " " << fill << ' ' << h << ' ' << i << endl;
  if (y < 0 || y >= Y || x < 0 || x >= X || G[y][x] == '#') {
    return true;
  }
  if (G[y][x] == '-' || G[y][x] == '|' || G[y][x] == 'X') return false;
  if (G[y][x] == '.' && fill) {
//cout << x << ',' << y << ' ' << ((dy==0)?'H':'V') << ' ' << i << ' ' << h << endl;
    ((dy==0) ? hv : vv)[y][x] = i;
    ((dy==0) ? hvh : vvh)[y][x] = h;
  }
  if (G[y][x] == '/') {
    swap(dx, dy); dx = -dx; dy = -dy;
    return doit(x+dx, y+dy, dx, dy, fill, h, i);
  } else if (G[y][x] == '\\') {
    swap(dx, dy);
    return doit(x+dx, y+dy, dx, dy, fill, h, i);
  } else {
    return doit(x+dx, y+dy, dx, dy, fill, h, i);
  }
}

vector<int> value;
bool do2sat(int i, int v) {
//cout << "do2sat " << i << ' ' << v << endl;
  if (i == -1) return false;
  if (value[i] == v) return true;
  if (value[i] != -1) return false;
  value[i] = v;
  for (int y = 0; y < Y; y++)
  for (int x = 0; x < X; x++) if (G[y][x] == '.') {
    if (hv[y][x] == i && hvh[y][x] != v) {
      if (!do2sat(vv[y][x], vvh[y][x])) return false;
    }
    if (vv[y][x] == i && vvh[y][x] != v) {
      if (!do2sat(hv[y][x], hvh[y][x])) return false;
    }
  }
  return true;
}

int main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    cin >> Y >> X;
    G.resize(Y);
    for (int y = 0; y < Y; y++) cin >> G[y];

    bx.clear(); by.clear();
    memset(hv, -1, sizeof(hv));
    memset(vv, -1, sizeof(vv));
    for (int y = 0; y < Y; y++)
    for (int x = 0; x < X; x++) {
      if (G[y][x] == '|' || G[y][x] == '-') {
        G[y][x] = 'X';
        if (doit(x-1, y, -1, 0, false) && doit(x+1, y, 1, 0, false)) {
          doit(x-1, y, -1, 0, true, 1, bx.size());
          doit(x+1, y, 1, 0, true, 1, bx.size());
          G[y][x] = '-';
        }
        if (doit(x, y-1, 0, -1, false) && doit(x, y+1, 0, 1, false)) {
          doit(x, y-1, 0, -1, true, 0, bx.size());
          doit(x, y+1, 0, 1, true, 0, bx.size());
          G[y][x] = '|';
        }
        if (G[y][x] == 'X') goto fail;
        bx.push_back(x);
        by.push_back(y);
      }
    }

    for (int y = 0; y < Y; y++)
    for (int x = 0; x < X; x++) if (G[y][x] == '.') {
      if (hv[y][x] == -1 && vv[y][x] == -1) goto fail;
    }

    value = vector<int>(bx.size(), -1);
    for (int i = 0; i < bx.size(); i++) if (value[i] == -1) {
      vector<int> value2 = value;
      if (do2sat(i, 0)) {
        continue;
      }
      value = value2;
      if (do2sat(i, 1)) {
        continue;
      }
      goto fail;
    }

    for (int i = 0; i < bx.size(); i++) {
      G[by[i]][bx[i]] = (value[i] ? '-' : '|');
    }
    cout << "Case #" << prob++ << ": POSSIBLE" << endl;
    for (int y = 0; y < Y; y++) cout << G[y] << endl;
    continue;

fail:
    cout << "Case #" << prob++ << ": IMPOSSIBLE" << endl;
  }
}
