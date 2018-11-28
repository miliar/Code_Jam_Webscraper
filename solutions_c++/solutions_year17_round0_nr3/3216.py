#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

typedef long long lol;
typedef vector<int> VI;
typedef vector<VI> VVI;

#define Loop(i, a, b) for (int i = (a); i < (b); ++i)
#define Loopb(i, a, b) for (int i = (a - 1); i >= (b); --i)

lol find(lol n) {
  lol ret = lol(1);
  for (lol k = n; k > 0; ret *= 2) k /= 2;
  return ret / 2;
}

int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  //freopen("C-small-2-attempt0.in", "rt", stdin);
  freopen("C-large.in", "rt", stdin);
  freopen("outputC.txt", "w", stdout);
#endif

  int line_num;
  cin >> line_num;
  for (int line = 0; line < line_num; ++line) {
    lol n, k, ans1, ans2;
    cin >> n >> k;
    VI vec;
    lol mod = find(k);
    n -= mod - 1;
    lol res = n / mod;
    lol left = n - mod * res;
    k -= mod - 1;
    if (k > left) --res;
      ans1 = res / 2; ans2 = res - ans1;
      printf("Case #%d: %ld %ld\n", line+1, ans2, ans1);
  }
  return 0;
}
