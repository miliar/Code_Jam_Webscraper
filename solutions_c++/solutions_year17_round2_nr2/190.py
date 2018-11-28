#include <bits/stdc++.h>

#define FOR(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

#define x first
#define y second

using namespace std;

typedef long long ll;

const int MAXN = 1010;

int n, r, y, b, ry, br, by;

enum Colors {
  BLUE, RED, YELLOW, ORANGE, GREEN, VIOLET
};

inline ll HASH(int R, int B, int Y, int RY, int BR, int BY, int last) {
  ll H = last;
  for (int x : vector<int>{R, B, Y, RY, BR, BY})
    H = H * 1000 + x;
  return H;
}

unordered_map<ll, ll> dad;
unordered_map<ll, bool> cache;
int first;
int bits[8];

bool f(int N, int R, int B, int Y, int RY, int BR, int BY, int last) {
  if (2*R-1 > N) return false;
  if (2*B-1 > N) return false;
  if (2*Y-1 > N) return false;
  if (RY-1 > B) return false;
  if (BR-1 > Y) return false;
  if (BY-1 > R) return false;
  if (R < 0) return false;
  if (B < 0) return false;
  if (Y < 0) return false;
  if (RY < 0) return false;
  if (BR < 0) return false;
  if (BY < 0) return false;

  if (N == 0) return (bits[last] & bits[first]) == 0;

  ll H = HASH(R, B, Y, RY, BR, BY, last);
  if (cache.count(H))
    return cache[H];

  if (last == BLUE) {
    // BLUE
    if (f(N-1, R-1, B, Y, RY, BR, BY, RED)) {
      dad[H] = HASH(R-1, B, Y, RY, BR, BY, RED);
      return cache[H] = true;
    }
    if (f(N-1, R, B, Y-1, RY, BR, BY, YELLOW)) {
      dad[H] = HASH(R, B, Y-1, RY, BR, BY, YELLOW);
      return cache[H] = true;
    }
    if (f(N-1, R, B, Y, RY-1, BR, BY, ORANGE)) {
      dad[H] = HASH(R, B, Y, RY-1, BR, BY, ORANGE);
      return cache[H] = true;
    }
  }
  
  if (last == RED) {
    // BLUE
    if (f(N-1, R, B-1, Y, RY, BR, BY, BLUE)) {
      dad[H] = HASH(R, B-1, Y, RY, BR, BY, BLUE);
      return cache[H] = true;
    }
    if (f(N-1, R, B, Y-1, RY, BR, BY, YELLOW)) {
      dad[H] = HASH(R, B, Y-1, RY, BR, BY, YELLOW);
      return cache[H] = true;
    }
    if (f(N-1, R, B, Y, RY, BR, BY-1, GREEN)) {
      dad[H] = HASH(R, B, Y, RY, BR, BY-1, GREEN);
      return cache[H] = true;
    }
  }
  
  if (last == YELLOW) {
    // BLUE
    if (f(N-1, R-1, B, Y, RY, BR, BY, RED)) {
      dad[H] = HASH(R-1, B, Y, RY, BR, BY, RED);
      return cache[H] = true;
    }
    if (f(N-1, R, B-1, Y, RY, BR, BY, BLUE)) {
      dad[H] = HASH(R, B-1, Y, RY, BR, BY, BLUE);
      return cache[H] = true;
    }
    if (f(N-1, R, B, Y, RY, BR-1, BY, VIOLET)) {
      dad[H] = HASH(R, B, Y, RY, BR-1, BY, VIOLET);
      return cache[H] = true;
    }
  }

  if (last == ORANGE) {
    if (f(N-1, R, B-1, Y, RY, BR, BY, BLUE)) {
      dad[H] = HASH(R, B-1, Y, RY, BR, BY, BLUE);
      return cache[H] = true;
    }
  }
  if (last == GREEN) {
    if (f(N-1, R-1, B, Y, RY, BR, BY, RED)) {
      dad[H] = HASH(R-1, B, Y, RY, BR, BY, RED);
      return cache[H] = true;
    }
  }
  if (last == VIOLET) {
    if (f(N-1, R, B, Y-1, RY, BR, BY, YELLOW)) {
      dad[H] = HASH(R, B, Y-1, RY, BR, BY, YELLOW);
      return cache[H] = true;
    }
  }

  return cache[H] = false;
}

void solve() {
  scanf("%d%d%d%d%d%d%d", &n, &r, &ry, &y, &by, &b, &br);
  
  static char ans[MAXN];
  memset(ans, 0, sizeof ans);
  bits[BLUE] = 1;
  bits[RED] = 2;
  bits[YELLOW] = 4;
  bits[ORANGE] = 6;
  bits[GREEN] = 5;
  bits[VIOLET] = 3;
  cache.clear();
  dad.clear();
  
  bool ok = false;
  if (r) first = RED, r--;
  else if (y) first = YELLOW, y--;
  else if (b) first = BLUE, b--;
  else if (br) first = VIOLET, br--;
  else if (by) first = GREEN, by--;
  else if (ry) first = ORANGE, ry--;
  
  if (!f(n-1, r, b, y, ry, br, by, first)) {
    printf("IMPOSSIBLE\n");
    return;
  }

  ll curr_hash = HASH(r, b, y, ry, br, by, first);
  REP(i, n) {
    int color = curr_hash / 1000000000000000000LL;
    if (color == RED) ans[i] = 'R';
    else if (color == BLUE) ans[i] = 'B';
    else if (color == GREEN) ans[i] = 'G';
    else if (color == YELLOW) ans[i] = 'Y';
    else if (color == VIOLET) ans[i] = 'V';
    else if (color == ORANGE) ans[i] = 'O';
    else ans[i] = 'X';
    curr_hash = dad[curr_hash];
  }

  printf("%s\n", ans);
}

int main(void) {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    solve();
  }
  return 0;
}

