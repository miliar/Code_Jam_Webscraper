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
const int N = 5e3+5;

int out[N];

int main() {
  freopen("output.txt", "w", stdout);
  int t, n, cas = 1;
  int a[6], b[3];
  char s[] = "RYB";
  scanf("%d", &t);
  while (t--) {
    memset(out, -1, sizeof out);
    scanf("%d", &n);
    for (int i = 0; i < 6; i++) {
      scanf("%d", a + i);
      if (i % 2 == 0) b[i/2] = a[i];
    }
    int pos = max_element(b, b + 3) - b;
    if (b[pos] * 2 > n) {
      if (n == 1) {
        printf("Case #%d: %c\n", cas++, s[pos]);
      } else {
        printf("Case #%d: IMPOSSIBLE\n", cas++);
      }
    } else {
      for (int i = 0; i < b[pos]; i++) {
        out[i*2] = pos;
      }
      bool fail = false;
      vector<int> v;
      for (int i = 0; i < 3; i++) if (i != pos) v.push_back(i);
      for (int i = 1; i < n; i++) {
        if (out[i] != -1) continue;
        int choice;
        if (out[i-1] == pos) {
          choice = b[v[0]] < b[v[1]] ? v[1] : v[0];
        } else {
          choice = 3 - out[i-1] - pos;
        }
        b[choice]--;
        out[i] = choice;
        fail |= b[choice] < 0;
      }

      for (int i = 0; i < n; i++) {
        fail |= out[i] == -1;
        int l = (i-1+n) % n, r = (i+1) % n;
        fail |= out[l] == out[i] || out[r] == out[i];
      }
      if (fail) {
        printf("Case #%d: IMPOSSIBLE\n", cas++);
      } else {
        printf("Case #%d: ", cas++);
        for (int i = 0; i < n; i++) {
          putchar(s[out[i]]);
        }
        puts("");
      }
    }
  }
  return 0;
}
