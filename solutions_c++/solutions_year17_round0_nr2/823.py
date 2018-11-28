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
char s[25];
int ck() {
  int n = strlen(s);
  for (int i = 1; i < n; i++) {
    if (s[i-1] > s[i]) return i-1;
  }
  return -1;
}

int brute(int x) {
  for (int i = x; i >= 1; i--) {
    sprintf(s, "%d", i);
    if (ck() == -1) return i;
  }
}

int main() {
  freopen("output.txt", "w", stdout);
  int t, cas = 1;
  scanf("%d", &t);
  while (t--) {
    scanf("%s", s);
    LL x, sub;
    sscanf(s, "%I64d", &x);
    printf("Case #%d: ", cas++);
    int pos = ck();
    LL ans = x;
    if (pos != -1) {
      while (pos > 0 && s[pos-1] == s[pos]) pos--;
      sscanf(s + pos + 1, "%I64d", &sub);
      ans -= sub + 1;
    }
    printf("%I64d\n", ans);
  }
  return 0;
}
