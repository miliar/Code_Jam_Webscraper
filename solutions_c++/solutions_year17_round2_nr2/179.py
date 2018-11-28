#include <bits/stdc++.h>
using namespace std;

const string C = "ROYGBV";
const string FAIL = "IMPOSSIBLE";

int T;
int N;
int r, o, y, g, b, v;
int cr, cy, cb;
int cntr, cnty, cntb;
string res;

inline char get_next() {
  if (r > max(y, b)) {
    if (res.empty() || res.back() != 'R') {
      --r;
      return 'R';
    } else if (y > b) {
      --y;
      return 'Y';
    } else {
      --b;
      return 'B';
    }
  } else if (y > max(b, r)) {
    if (res.empty() || res.back() != 'Y') {
      --y;
      return 'Y';
    } else if (b > r) {
      --b;
      return 'B';
    } else {
      --r;
      return 'R';
    }
  } else if (b > max(r, y)) {
    if (res.empty() || res.back() != 'B') {
      --b;
      return 'B';
    } else if (r > y) {
      --r;
      return 'R';
    } else {
      --y;
      return 'Y';
    }
  } else {
    if (res.empty()) {
      if (r > 0) {
        --r;
        return 'R';
      } else if (y > 0) {
        --y;
        return 'Y';
      } else if (b > 0) {
        --b;
        return 'B';
      }
    } else if (res[0] == 'R') {
      if (res.back() == 'R') {
        if (y > 0) {
          --y;
          return 'Y';
        } else {
          --b;
          return 'B';
        }
      } else {
        --r;
        return 'R';
      }
    } else if (res[0] == 'Y') {
      if (res.back() == 'Y') {
        if (b > 0) {
          --b;
          return 'B';
        } else {
          --r;
          return 'R';
        }
      } else {
        --y;
        return 'Y';
      }
    } else if (res[0] == 'B') {
      if (res.back() == 'B') {
        if (r > 0) {
          --r;
          return 'R';
        } else {
          --y;
          return 'Y';
        }
      } else {
        --b;
        return 'B';
      }
    } else {
      cerr << "GLOBAL FAIL" << endl;
      assert(false);
    }
  }
}

void solve_small() {
  while (r + y + b) {
    res += get_next();
  }
}

string solve() {
  res.clear();
  
  cin >> N;
  cin >> r >> o >> y >> g >> b >> v;

  r -= g;
  y -= v;
  b -= o;

  if (r == 0 && g > 0) {
    if (y > 0 || v > 0 || b > 0 || o > 0) {
      return FAIL;
    } else {
      for (int i = 0; i < g; ++i) {
        res += 'R';
        res += 'G';
      }
      return res;
    }
  }

  if (y == 0 && v > 0) {
    if (b > 0 || o > 0 || r > 0 || g > 0) {
      return FAIL;
    } else {
      for (int i = 0; i < v; ++i) {
        res += 'Y';
        res += 'V';
      }
      return res;
    }
  }

  if (b == 0 && o > 0) {
    if (r > 0 || g > 0 || y > 0 || v > 0) {
      return FAIL;
    } else {
      for (int i = 0; i < o; ++i) {
        res += 'B';
        res += 'O';
      }
      return res;
    }
  }
  
  if (r + y < b ||
      y + b < r ||
      b + r < y ||
      (r <= 0 && g > 0) ||
      (y <= 0 && v > 0) ||
      (b <= 0 && o > 0)) {
    res = FAIL;
  } else {
    solve_small();
    for (int i = 0; i < res.size(); ++i) {
      if (res[i] == 'R') {
        for (int j = 0; j < g; ++j) {
          res.insert(i, 1, 'G');
          res.insert(i, 1, 'R');
        }
        break;
      }
    }
    for (int i = 0; i < res.size(); ++i) {
      if (res[i] == 'Y') {
        for (int j = 0; j < v; ++j) {
          res.insert(i, 1, 'V');
          res.insert(i, 1, 'Y');
        }
        break;
      }
    }
    for (int i = 0; i < res.size(); ++i) {
      if (res[i] == 'B') {
        for (int j = 0; j < o; ++j) {
          res.insert(i, 1, 'O');
          res.insert(i, 1, 'B');
        }
        break;
      }
    }
  }

  return res;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: %s\n", test, solve().c_str());
  }
}
