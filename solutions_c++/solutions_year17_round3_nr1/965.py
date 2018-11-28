#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR0(A,n) { cout << #A << " = "; FORN(_,n) cout << A[_] << ' '; cout << endl; }

// #define FL fflush(stdout)

#define MOD 1000000007
#define INF 2000000000
#define maxn 1010

int GLL(LL& x) {
  return scanf("%lld", &x);
}

int GI(int& x) {
  return scanf("%d", &x);
}

int N, K;
vector<pair<double, double> > rh;
map<LL, vector<LL> > pan;
vector<pair<double, int> > sides;
double eps = 0.0000000001;

void solve(int t) {
  map<LL, vector<LL> > empty; swap(empty, pan);
  GI(N); GI(K);
  rh.resize(N);

  vector<double> sides;
  FORN(i, N) {
    LL r, h; GLL(r); GLL(h);
    pan[r].PB(h);
    sides.PB(2 * M_PI * r * h);
  }
  sort(sides.begin(), sides.end());

  for (auto& kv : pan) {
    sort(kv.SS.begin(), kv.SS.end());
  }

  double ans = 0, maxans = 0;
  for (auto& kv: pan) {
//    printf("bottom: %d, %d\n", kv.FF, kv.SS[kv.SS.size()-1]);
    ans = 0;
    ans += kv.FF * kv.FF * M_PI;
    double cside = 2 * M_PI * kv.FF * kv.SS[kv.SS.size() - 1];
    ans += cside;

    int count = 0;
    bool flag = false;
    
    vector<double> sides;
    for (auto& kv2 : pan) {
      if (kv2.FF > kv.FF) continue;

      for (auto h : kv2.SS) {
//        printf("h: %d\n", h);
        if (flag==false && (kv2.FF == kv.FF && h == kv.SS[kv.SS.size() - 1])) {
//          printf("current pancake found: (%d, %d)\n", kv2.FF, h);
          flag = true;
          continue;
        }
        sides.PB(2 * M_PI * kv2.FF * h);
      }
    }
    sort(sides.begin(), sides.end());
//    printf("here %d\n", sides.size());
//    FORN(i, sides.size()) printf("%f ", sides[i]); printf("\n");

    if (sides.size() < K-1) {
      continue;
    }
    FOR1(i, K-1) {
      int idx = sides.size()-i;
//      printf("    + sides[%d] = %f\n", idx, sides[idx]);
      ans += sides[idx];
    }

    maxans = max(ans, maxans);
  }
  printf("Case #%d: %.20f\n", t+1, maxans);
}

int T;
int main() {
  GI(T);
  for (int t = 0; t < T; t++) {
    solve(t);
  }
  return 0;
}
