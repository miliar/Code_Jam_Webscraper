#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef pair<int, int> P;
typedef pair<P, char> PP;

const string IMP = "IMPOSSIBLE";

string intercala(int n, char x, char y) {
  string res;
  for (int i = 0; i < n; ++i) {
    res += x;
    res += y;
  }
  return res;
}

char select(int r, int y, int b, char prev, char favor) {
  vector<PP> vec;
  if (prev != 'R') {
    vec.push_back(PP(P(r, favor == 'R' ? 1 : 0), 'R'));
  }
  if (prev != 'Y') {
    vec.push_back(PP(P(y, favor == 'Y' ? 1 : 0), 'Y'));
  }
  if (prev != 'B') {
    vec.push_back(PP(P(b, favor == 'B' ? 1 : 0), 'B'));
  }
  PP m(P(-1, -1), ' ');
  for (int i = 0; i < int(vec.size()); ++i) {
    m = max(m, vec[i]);
  }
  return m.second;
}

char check(int r, int y, int b, char color) {
  if (color == 'R') {
    return r > 0;
  }
  if (color == 'Y') {
    return y > 0;
  }
  return b > 0;
}

void decr(int& r, int& y, int& b, char color) {
  if (color == 'R') {
    --r;
  } else if (color == 'Y') {
    --y;
  } else {
    --b;
  }
}

string fun(int r, int o, int y, int g, int b, int v) {
  int n = r + o + y + g + b + v;
  if (o != 0) {
    if (o == b && o + b == n) {
      return intercala(o, 'B', 'O');
    }
    if (o >= b) {
      return IMP;
    }
  }
  if (g != 0) {
    if (g == r && g + r == n) {
      return intercala(g, 'R', 'G');
    }
    if (g >= r) {
      return IMP;
    }
  }
  if (v != 0) {
    if (v == y && v + y == n) {
      return intercala(v, 'Y', 'V');
    }
    if (v >= y) {
      return IMP;
    }
  }
  b -= o;
  r -= g;
  y -= v;
  string res;
  char prev = ' ';
  while (r + y + b > 0) {
    char color = select(r, y, b, prev, res.size() > 0 ? res[0] : ' ');
    if (!check(r, y, b, color)) {
      return IMP;
    }
    decr(r, y, b, color);
    if (color == 'R' && g > 0) {
      res += intercala(g, 'R', 'G');
      g = 0;
    }
    if (color == 'Y' && v > 0) {
      res += intercala(v, 'Y', 'V');
      v = 0;
    }
    if (color == 'B' && o > 0) {
      res += intercala(o, 'B', 'O');
      o = 0;
    }
    res += color;
    prev = color;
  }
  if (res.size() > 1 && res[0] == res[res.size() - 1]) {
    return IMP;
  }
  return res;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    cout << "Case #" << cas << ": " << fun(r, o, y, g, b, v) << endl;
  }
}
