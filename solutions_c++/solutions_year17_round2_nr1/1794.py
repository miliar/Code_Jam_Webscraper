#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
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
#define MAXN 1010

int GLL(LL& x) {
  return scanf("%lld", &x);
}

int GI(int& x) {
  return scanf("%d", &x);
}

void solve(int t) {
  LL D, N;
  vector<pair<LL, LL> > horses;
//  LL x[MAXN], v[MAXN];  
  GLL(D); GLL(N);
  FORN(i, N) {
    LL x, v;
    GLL(x); GLL(v);
    horses.PB(MP(D - x, v));
  }
//  sort(horses.begin(), horses.end());

  double maxt = 0;
  FORN(i, N) {
    auto h = horses[i];
    double t = (h.FF + 0.0) / (h.SS);
    if (t > maxt) maxt = t;
  }

//  printf("maxt: %f, D: %d, %f\n", maxt, D, (D+0.0)/maxt);

  double ans = (D+0.0)/maxt;

//  printf("\n");
//  printf("\n");
//  FORN(i, N) {
//    printf("%d, %d\n", horses[i].FF, horses[i].SS);
//  }
  printf("Case #%d: %f\n", t+1, ans);
}

int T;
int main() {
  GI(T);
  for (int t = 0; t < T; t++) {
    solve(t);
  }
  return 0;
}
