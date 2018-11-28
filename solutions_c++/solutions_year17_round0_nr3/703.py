#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long int64;

void solve() {
  int64 n, k;
  scanf("%lld%lld", &n, &k);
  while (k > 1) {
    if (k & 1) {
      n = n - 1 - n / 2;
    } else {
      n /= 2;
    }
    k /= 2;
  }
  int64 y = (n + 1) / 2;
  printf("%lld %lld\n", n - y, y - 1);
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: ", index);
    solve();
  }
  return 0;
}
