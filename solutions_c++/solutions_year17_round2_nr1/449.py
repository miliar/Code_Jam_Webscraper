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

int main() {
  freopen("output.txt", "w", stdout);
  int t, d, n, a, b, cas = 1;
  scanf("%d", &t);
  while (t--) {
    scanf("%d%d", &d, &n);
    double ans = -1;
    for (int i = 0; i < n; i++) {
      scanf("%d%d", &a, &b);
      ans = max(ans, double(d - a) / b);
    }
    printf("Case #%d: %.6f\n", cas++, d / ans);
  }
  return 0;
}
