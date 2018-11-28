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

const int MAXN = 55;
double ar[MAXN];
double ans[MAXN][MAXN];

// zero any arrays
void reset() {
  memset(ans, 0, sizeof(ans));
}

void add(double p, int s, int t) {
  if (s == t) return; // 0 case
  for(int i = s; i < t; ++i) {
    ar[i] += p / (t - s);
  }
}

void spend(double P, int s, int t) {
  int cnt = 0;
  double cur = 0;
  for(int i = s; i <= t; ++i) {
    double cost = ((i == t ? 1 : ar[i]) - cur) * cnt;
    if (cost > P) {
      add(P, s, i);
      P = 0;
    } else {
      add(cost, s, i);
      P -= cost;
    }

    cur = ar[i];
    ++cnt;
  }
}


// read an input from stdin, solve, print output to stdout
void solve_case() {
  reset();
  int N, K;
  scanf("%d %d", &N, &K);
  double P;
  scanf("%lf", &P);

  for(int i = 0; i < N; ++i) {
    scanf("%lf", ar + i);
  }
  sort(ar, ar + N);
  spend(P, N - K, N);

  ans[0][0] = 1;
  for(int t = 0; t < N; ++t) {
    for(int i = 0; i < N; ++i) {
      ans[t + 1][i + 0] += ans[t][i] * (1 - ar[t]);
      ans[t + 1][i + 1] += ans[t][i] * ar[t];
    }
  }

  double finalAns = 0;
  for(int k = K; k <= N; ++k) {
    finalAns += ans[N][k];
  }
  printf("%.9lf\n", finalAns);
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
