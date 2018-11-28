#include <bits/stdc++.h>

using namespace std;

#ifdef ACMTUYO
struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#else
struct RTC{};
#define DBG(X)
#endif

#define fast_io() ios_base::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long int number;
const int maxn = 1010;
char s[maxn];
int cnt[maxn];
int k;
int main() {
  int ntc;
  scanf("%d", &ntc);
  for (int tc = 1; tc <= ntc; tc++) {
    scanf("%s %d", s, &k);
    memset(cnt, 0, sizeof(cnt));
    int ans = 0, cur = 0, n = strlen(s);
    forn (i, n) {
      cur += cnt[i];
      assert(cur >= 0);
      char c = s[i];
      if (cur & 1)//invertido
        c = (c=='+')?'-':'+';
      if (c == '-') {
        ans++;
        if (i + k <= n) {
          cur++;
          cnt[i + k]--;
        } else {
          ans = -1;
          break;
        }
      }
    }
    printf("Case #%d: ", tc);
    if (ans < 0)
      puts("IMPOSSIBLE"); 
    else
      printf("%d\n", ans);
  }
  return 0;
}
