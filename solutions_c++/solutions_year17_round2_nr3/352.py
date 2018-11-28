#define NDEBUG
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long int64;
template<typename T, typename U> inline bool makemin(T &res, const U &x) {
  if (x < res) {
    res = x;
    return true;
  }
  return false;
}
#define repeat(n) for (int repc = (n); repc > 0; --repc)

const int MAXN = 105;
const int64 INF = LONG_LONG_MAX / 4;

string solve() {
  int N, Q;
  cin >> N >> Q;
  vector<int> E(N), S(N);
  for (int i = 0; i < N; ++i) {
    cin >> E[i] >> S[i];
  }

  int64 dist[MAXN][MAXN];
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      cin >> dist[i][j];
      if (dist[i][j] < 0) dist[i][j] = INF;
    }
  }

  for (int j = 0; j < N; ++j) {
    for (int i = 0; i < N; ++i) {
      for (int k = 0; k < N; ++k) {
        makemin(dist[i][k], dist[i][j] + dist[j][k]);
      }
    }
  }

  double d2[MAXN][MAXN];
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      d2[i][j] = dist[i][j] <= E[i] ? double(dist[i][j]) / S[i] : HUGE_VAL;
    }
  }
  for (int j = 0; j < N; ++j) {
    for (int i = 0; i < N; ++i) {
      for (int k = 0; k < N; ++k) {
        makemin(d2[i][k], d2[i][j] + d2[j][k]);
      }
    }
  }
  string out;
  repeat (Q) {
    int a, b;
    cin >> a >> b;
    --a; --b;
    char buf[100];
    assert(!std::isinf(d2[a][b]));
    sprintf(buf, " %.10f", d2[a][b]);
    out += buf;
  }
  return out;
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ":" << solve() << endl;
  }
}
