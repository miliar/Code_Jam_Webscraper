#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
// head
map<LL, LL, greater<LL> > ma;
int main() {
  freopen("output.txt", "w", stdout);
  int t, cas = 1;
  LL x, k;
  scanf("%d", &t);
  while (t--) {
    scanf("%I64d%I64d", &x, &k);
    ma[x]++;
    printf("Case #%d: ", cas++);
    while (true) {
      LL cur = ma.begin()->fi;
      LL cnt = ma.begin()->se;
      LL a = (cur - 1) / 2;
      LL b = cur - 1 - a;
      if (cnt >= k) {
        printf("%I64d %I64d\n", b, a);
        break;
      } else {
        ma[a] += cnt;
        ma[b] += cnt;
        ma.erase(ma.begin());
        k -= cnt;
      }
    }
    ma.clear();
  }
  return 0;
}
