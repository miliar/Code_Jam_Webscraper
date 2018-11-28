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
const int N = 105;

int a[5];
int main() {
  freopen("output.txt", "w", stdout);
  int t, cas = 1, p, x, n;
  scanf("%d", &t);
  while (t--) {
    memset(a, 0, sizeof a);
    scanf("%d%d", &n, &p);
    for (int i = 0; i < n; i++) {
      scanf("%d", &x);
      a[x%p]++;
    }
    int ans = 0;
    if (p == 2) {
      ans = a[0] + (a[1] + 1) / 2;
    } else if (p == 3) {
      ans = a[0];
      int temp = min(a[1], a[2]);
      ans += temp;
      ans += (a[1] + a[2] - 2 * temp + 2) / 3;
    } else {
      ans = a[0];
      ans += a[2] / 2;
      a[2] &= 1;
      int temp = min(a[1], a[3]);
      ans += temp;
      a[1] -= temp;
      a[3] -= temp;
      if (a[2]) {
        ans++;
        ans += (a[1] + a[3] - 2 + 3) / 4;
      } else {
        ans += (a[1] + a[3] + 3) / 4;
      }
    }
    printf("Case #%d: %d\n", cas++, ans);
  }
  return 0;
}
