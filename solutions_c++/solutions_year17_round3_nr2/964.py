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

int ac, aj;
//int c[maxn][2], j[maxn][2];

void solve(int t) {
  vector< pair<int, int> > c, j;
  GI(ac);
  GI(aj);
  FORN(i, ac) { 
    int a, b;
    GI(a); GI(b);
    c.PB(MP(a, b));
  }
  FORN(i, aj) { 
    int a, b;
    GI(a); GI(b);
    j.PB(MP(a, b));
  }


  sort(c.begin(), c.end());
  sort(j.begin(), j.end());
 
  int ans = 2;
//  printf("   C -----------------------\n"); for (auto ab : c) printf("   (%d, %d)\n", ab.FF, ab.SS);
//  printf("   J -----------------------\n"); for (auto ab : j) printf("   (%d, %d)\n", ab.FF, ab.SS);
  if (ac < 2 && aj < 2) {
    printf("Case #%d: %d\n", t+1, 2);
    return;
  }
  if (ac > 1) {
    int try1 = c[1].SS - c[0].FF;
    int try2 = c[0].SS - c[1].FF + 1440;
//    printf("   %d - %d + 1440\n", c[0].SS, c[1].FF);
//    printf("   %d, %d\n", try1, try2);

    if (try1 > 720 && try2 > 720) ans=4;
  }

  if (aj > 1) {
    int try1 = j[1].SS - j[0].FF;
    int try2 = j[0].SS - j[1].FF + 1440;
//    printf("%d, %d\n", try1, try2);

    if (try1 > 720 && try2 > 720) ans=4;
  }

  printf("Case #%d: %d\n", t+1, ans);
}

int T;
int main() {
  GI(T);
  for (int t = 0; t < T; t++) {
    solve(t);
  }
  return 0;
}
