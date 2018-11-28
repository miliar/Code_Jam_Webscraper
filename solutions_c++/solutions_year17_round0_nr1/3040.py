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
#define maxn 1010

int GLL(LL& x) {
  return scanf("%lld", &x);
}

int GI(int& x) {
  return scanf("%d", &x);
}

void solve(int t) {
  string s;
  int k;
  bool pan[maxn];
  cin >> s >> k;

  for (int i = 0; i < s.size(); i++) {
    bool b = (s[i] == '-') ? false : true;
    pan[i] = b;
  }

  int pos = 0;
  int count = 0;
  while (pos + k <= s.size()) {
    if (pan[pos] == 0) {
      FORN(j, k) pan[pos+j] = pan[pos+j]^1;
      count++;
    };
    pos++;
  }

//  for (int i = 0; i < s.size(); i++) printf("%d ", pan[i]); printf("\n");

  for (int i = 0; i < s.size(); i++) {
    if (!pan[i]) {
      printf("Case #%d: IMPOSSIBLE\n", t+1);
      return;
    }
  }
  printf("Case #%d: %d\n", t+1, count);
}

int T;
int main() {
  GI(T);
  for (int t = 0; t < T; t++) {
    solve(t);
  }
  return 0;
}
