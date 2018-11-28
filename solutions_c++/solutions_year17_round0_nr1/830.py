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
const int N = 1e3+5;

char s[N];
bool a[N];
int main() {
  freopen("output.txt", "w", stdout);
  int t, k, cas = 1;
  scanf("%d", &t);
  while (t--) {
    scanf("%s%d", s, &k);
    int n = strlen(s), ans = 0;
    for (int i = 0; i < n; i++) a[i] = s[i] == '+';
    for (int i = 0; i <= n - k; i++) {
      if (a[i] == 0) {
        ans++;
        for (int j = 0; j < k; j++) a[i+j] = !a[i+j];
      }
    }
    printf("Case #%d: ", cas++);
    if (*min_element(a, a + n) == 0) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", ans);
    }
  }
  return 0;
}
