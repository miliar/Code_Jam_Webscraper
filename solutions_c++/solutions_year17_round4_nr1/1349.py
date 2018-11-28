#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long int64;

int n, p;
vector<int> a;

int f2() {
  int ans = 0, c = 0;
  for (int x : a) {
    if (x % 2 == 1) {
      ++c;
    } else {
      ++ans;
    }
  }
  return ans + (c + 1) / 2;
}

int f3() {
  int c1 = 0, c2 = 0, ans = 0;
  for (int x : a) {
    if (x % 3 == 0) {
      ++ans;
    } else if (x % 3 == 1) {
      ++c1;
    } else {
      ++c2;
    }
  }
  int c = min(c1, c2);
  c1 -= c;
  c2 -= c;
  return ans + c + (c1 + 2) / 3 + (c2 + 2) / 3;
}

int f4() {
  int c1 = 0, c2 = 0, c3 = 0, ans = 0, d;

  for (int x : a) {
    if (x % 4 == 0) ++ans;
    else if (x % 4 == 1) ++c1;
    else if (x % 4 == 2) ++c2;
    else ++c3;
  }

  d = min(c1, c3);
  c1 -= d, c3 -= d;
  ans += d;

  d = min(c1 / 2, c2);
  c1 -= 2 * d, c2 -= d;
  ans += d;

  d = min(c3 / 2, c2);
  c3 -= 2 * d, c2 -= d;
  ans += d;

  d = c2 / 2;
  c2 -= 2 * d;
  ans += d;

  d = c1 / 4;
  c1 -= 4 * d;
  ans += d;

  d = c3 / 4;
  c3 -= 4 * d;
  ans += d;

  if (c1 != 0 || c2 != 0 || c3 != 0) ++ans;
  return ans;
}

int solve() {
  scanf("%d%d", &n, &p);

  a.resize(n);
  REP (i, n) scanf("%d", &a[i]);

  if (p == 2) return f2();
  if (p == 3) return f3();
  if (p == 4) return f4();

  assert(false);
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %d\n", index, solve());
  }
  return 0;
}
