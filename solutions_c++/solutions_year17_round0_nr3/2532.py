#include <bits/stdc++.h>
using namespace std;

int main() {
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w+", stdout);
  int T;
  long long N, K, ls, rs, lt, rt;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    cin >> N >> K;
    ls = N/2;
    rs = (N-1)/2;
    lt = 1;
    rt = 1;
    K--;
    while (K > 0) {
      if (lt < K) {
        K -= lt;
      } else {
        rs = (ls-1)/2;
        ls = ls/2;
        break;
      }
      if (rt < K) {
        K -= rt;
      } else {
        ls = rs/2;
        rs = (rs-1)/2;
        break;
      }
      if (ls == rs) {
        lt = lt+rt;
        rt = lt;
      } else {
        if (rs%2) {
          rt = rt*2+lt;
        } else {
          lt = lt*2+rt;
        }
      }
      ls = (rs+(ls!=rs))/2;
      rs = (rs-1)/2;
    }
    printf("Case #%d: %lld %lld\n", t, ls, rs);
  }
  
  return 0;
}

