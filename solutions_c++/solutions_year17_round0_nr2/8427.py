#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdlib>
using namespace std;
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef long long ll;
int tc;
ll n;

ll next(ll num) {
  if (num < 10) return num;
  ll ret = next(num / 10);
  if (ret > num / 10) {
    return ret % 10 + ret * 10;
  }
  return max(num % 10, ret % 10) + ret * 10;
}

ll bsearch(ll lo, ll hi) {
  if (lo >= hi) return lo;
  ll mid = (lo + hi + 1) / 2;
  //printf("%lld\n", mid);
  ll f = next(mid);
  if (f > n) {
    return bsearch(lo, mid - 1);
  }
  return bsearch(mid, hi);
}

int main() {
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  cin >> tc;
  for (int i = 1; i <= tc; i++) {
    printf("Case #%d: ", i);
    cin >> n;
    printf("%lld\n", bsearch(1, 1000000000000000000L));
  }
  return 0;
}