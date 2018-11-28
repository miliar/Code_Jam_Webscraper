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
#include <cmath>
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
const double PI = acos(-1.);

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

// zero any arrays
void reset() {
}


const int MAXN = 1111;
typedef pair<double, double> pancake;

pancake ar[MAXN];

// read an input from stdin, solve, print output to stdout
void solve_case() {
  int N, K;
  reset();
  scanf("%d %d", &N, &K);
  for(int i = 0; i < N; ++i) {
    int _r, _h;
    scanf("%d %d", &_r, &_h);
    double r = _r, h = _h;
    ar[i] = pancake(2 * PI * r * h, PI * r * r);
  }
  sort(ar, ar + N);

  double sum = 0;
  for(int i = N - K + 1; i < N; ++i) {
    sum += ar[i].first;
  }
  double best = 0;
  for(int i = 0; i < N; ++i) {
    double flat_contrib = ar[i].second;
    double round_contrib = ar[i].first;
    if (i > N - K) { // already taking this one
      round_contrib = ar[N - K].first;
    }
    if (flat_contrib + round_contrib > best) {
      best = flat_contrib + round_contrib;
    }
  }

  double ans = sum + best;
  printf("%.9lf\n", ans);
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
