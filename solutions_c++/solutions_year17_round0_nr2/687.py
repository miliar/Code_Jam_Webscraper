#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long int64;

const int N = 20;

int n;
char s[N], t[N];

bool dfs(int i, int last, bool flag) {
  if (i == n) return true;
  if (!flag) {
    if (s[i] - '0' < last) return false;
    t[i] = s[i];
    if (dfs(i + 1, s[i] - '0', false)) return true;
    if (s[i] == '0' || s[i] - '0' - 1 < last) return false;
    t[i] = s[i] - 1;
    return dfs(i + 1, s[i] - '0' - 1, true);
  }
  t[i] = '9';
  return dfs(i + 1, 9, true);
}

void solve() {
  scanf("%s", s);
  n = strlen(s);
  dfs(0, 0, false);
  int i = 0;
  while (t[i] == '0') ++i;
  t[n] = '\0';
  printf("%s\n", t + i);
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
