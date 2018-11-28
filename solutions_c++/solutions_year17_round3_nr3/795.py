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

int n, k;
double u, eps = 0.000000000001;
vector<double> p;

double bs() {
  double lo = 0, hi = 1, guess = 0;

  while (lo <= hi) {
    double mid = (lo + hi) / 2;
    double res = 0;
    FORN(i, n) res += max(0.0, mid - p[i]);

    if ( u > res + eps ) {
      lo = mid + eps;
      guess = mid;
    }
    else hi = mid - eps;
    }
  return guess;
}


void solve(int t) {
  GI(n);
  GI(k);
  cin >> u;
  vector<double> empty; swap(empty, p);
  FORN(i, n) {
    double temp;
    cin >> temp;
    p.PB(temp);
  }

  double level = bs();
//  printf("max level: %.20f\n", level);
  double ans = 1;
  FORN(i, n) {
    ans *= max(level, p[i]);
  }

  printf("Case #%d: %.20f\n", t+1, ans);
}

int T;
int main() {
  GI(T);
  for (int t = 0; t < T; t++) {
    solve(t);
  }
  return 0;
}
