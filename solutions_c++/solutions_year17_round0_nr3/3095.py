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
#include <queue>


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

void solve(int t) {
  LL n, k;
  GLL(n);
  GLL(k);
  map<LL, LL> cnts;

  cnts[n]++;
  auto it = cnts.rbegin();
  while (k > 1) {
//    printf("k: %lld, it (%lld, %lld)\n", k, it->first, it->second);
    if (it->second >= k) break;
    k -= it->second;
    LL a1 = (it->first - 1)/2;
    LL a2 = (it->first - 1) - a1;

    cnts[a1] += it->second;
    cnts[a2] += it->second;
    it++;
  }

  LL a1 = (it->first - 1)/2;
  LL a2 = (it->first - 1) - a1;
//  printf("it: (%lld, %lld)\n", it->first, it->second);
  printf("Case #%d: %lld %lld\n", t+1, max(a1, a2), min(a1, a2));
}

int T;
int main() {
  GI(T);
  for (int t = 0; t < T; t++) {
    solve(t);
  }
  return 0;
}
