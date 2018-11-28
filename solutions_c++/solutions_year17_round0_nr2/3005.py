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
  string num; cin >> num;
  if (num.size() == 1) {
    printf("Case #%d: %s\n", t+1, num.c_str());
    return;
  }

  vector<int> dig;
  FORN(i, num.size()) {
    int d = num[i] - '0';
    dig.PB(d);
  }

  int idx;
  for (idx = 1; idx <= dig.size()-1; idx++) {
    if (dig[idx-1] > dig[idx]) break;
  }

  if (idx == dig.size()) {
    printf("Case #%d: %s\n", t+1, num.c_str());
    return;
  }

  idx--;
  while (idx >= 1 && dig[idx] - 1 < dig[idx-1]) {
    idx--;
  }
//  printf("\nidx:%d\n", idx);

  dig[idx]--;
  for (int i = idx+1; i < dig.size(); i++) dig[i] = 9;

  bool flag = false;
  printf("Case #%d: ", t+1);
  for (auto i : dig) {
    if (i != 0) flag = true;
    if (flag) printf("%d", i);
  }
  printf("\n");
}

int T;
int main() {
  GI(T);
  for (int t = 0; t < T; t++) {
    solve(t);
  }
  return 0;
}
