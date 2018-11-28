#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl

#define SIZE(a) ((int) a.size())

typedef pair<int, int> pii;

vector<long long> a;
int c[10];

long long solve(long long n) {
  if (n == (long long)(1e18)) {
    return n - 1;
  }

  int l = 0, r = SIZE(a) - 1;
  long long res = 1;

  while (l <= r) {
    int m = (l + r) / 2;
    if (a[m] <= n) {
      res = a[m];
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  return res;
}

long long makeNum() {
  long long num = 0;
  FOR (i, 1, 9) {
      for (int j = 1; j <= c[i]; j++) {
        num = num * 10 + i;
      }
  }

  return num;
}

void attempt(int d, int cnt) {
  if (d == 0) {
    long long x = makeNum();
    a.push_back(x);
    return;
  }

  for (int i = 1; cnt - i >= d - 1; i++) {
    c[d] = i - 1;
    attempt(d - 1, cnt  - i);
  }
}

int main() {
  attempt(9, 18 + 9);
  sort(a.begin(), a.end());

  int t;
  cin >> t;

  FOR (i, 1, t) {
    long long n;
    cin >> n;
    cout << "Case #" << i << ": " << solve(n) << endl;
  }

  return 0;
}
