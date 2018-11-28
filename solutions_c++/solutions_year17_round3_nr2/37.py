// FB Hacker Cup Template by Steven Hao
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <complex>
#include <functional>
#include <iostream>
#include <algorithm>
using namespace std;

// ==============================
// Typedefs, macros, constants

typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef long long ll;
typedef priority_queue<pii, vector<pii>, greater<pii> > PQ;
const int inf = 1000 << 20;
const ll infl = ll(inf) << 30; // slightly more than 10^18
const int MOD = 1E9 + 7;

#define SETMIN(x, y) do{if(y < x) x = y;}while(0)
#define SETMAX(x, y) do{if(y > x) x = y;}while(0)

// ==============================
// Debug helpers

// Uncomment this line to turn debugging on
// #define DEBUG

#ifdef DEBUG
#define RED_COLOR "\033[1;31m"
#define DEFAULT_COLOR "\033[1;39m"
// print to stdout to avoid stdoutout/stderr mixing
#define RED(x) do { cout << RED_COLOR; x; cout << DEFAULT_COLOR; } while(0)
#define P(x) RED(cout << #x << " " << x << "\n") // advanced printing
#define Q(x) RED(cout << x << "\n") // macro for "print"
#define PP(...) RED(fprintf (stdout, __VA_ARGS__)) // macro for printf
#define WHEN_DEBUG(x) x
#else
#define P(x)
#define Q(x)
#define PP(...)
#define WHEN_DEBUG(x)
#endif

// do any precomputation
void precompute() {

}

const int MAXN = 2222;
int N = 1440; // midnight

int busy[MAXN][2]; // busy[i][0] = 1 if person 0 is free at time i
int DP[2][2][MAXN][MAXN * 2];

// zero any arrays
void reset() {
  memset(DP, 0, sizeof(DP));
  memset(busy, 0, sizeof(busy));
}

int getDP(int end, int prv, int idx, int cnt) {
  if (idx == N) {
    if (cnt != 0) {
      return inf;
    } else {
      if (prv == end) { // no need to switch
        return 0;
      } else {
        return 1;
      }
    }
  }

  int &ret = DP[end][prv][idx][cnt + MAXN];
  if (ret) return ret - 1;
  ret = inf;
  for(int nxt = 0; nxt < 2; ++nxt) {
    if (busy[idx][nxt]) continue;
    int ncnt = cnt + (nxt == 0 ? 1 : -1);
    int add = nxt == prv ? 0 : 1;
    int cand = add + getDP(end, nxt, idx + 1, ncnt);
    if (cand < ret) ret = cand;
  }
  return ret++;
}

// read an input from stdin, solve, print output to stdout
void solve_case() {
  reset();
  int A, B;
  scanf("%d %d", &A, &B);
  for(int i = 0; i < A; ++i) {
    int s, t;
    scanf("%d %d", &s, &t);
    for(int j = s; j < t; ++j) {
      busy[j][0] = 1;
    }
  }
  for(int i = 0; i < B; ++i) {
    int s, t;
    scanf("%d %d", &s, &t);
    for(int j = s; j < t; ++j) {
      busy[j][1] = 1;
    }
  }

  int ans = inf;

  for(int start = 0; start < 2; ++start) {
    int cand = getDP(start, start, 0, 0);
    if (cand < ans) {
      ans = cand;
    }
  }
  printf("%d\n", ans);
}

// Main entry point
int main() {
  //precompute(); Q("done precomputing");

  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    PP("solving case %d\n", t);
    printf("Case #%d: ", t);
    solve_case();
  }
}
