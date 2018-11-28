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
int digits[30];
int n;
int m[30][2][10];
int okay(int pos, bool is_eq, int last_digit) {
  if (pos == n) return true;
  int &ans = m[pos][is_eq?1:0][last_digit];
  if (ans != -1) return ans;
  ans = -2;
  for (int digit = is_eq?digits[pos]:9; digit >= last_digit; digit--)
    if (okay(pos + 1, is_eq and digit == digits[pos], digit) >= 0)
      return (ans = digit);
  return ans;
}
char buff[30];
int main() {
  int ntc;
  scanf("%d", &ntc);
  for (int tc = 1; tc <= ntc; tc++) {
    scanf("%s", buff);
    n = strlen(buff);
    forn (i, n)
      digits[i] = buff[i] - '0';
    memset(m, -1, sizeof m);
    bool is_eq = true;
    int last_digit = 0;
    number ans = 0;
    for (int pos = 0; pos < n; pos++) {
      int digit = okay(pos, is_eq, last_digit);
      ans = ans * 10LL + digit;
      last_digit = digit;
      is_eq = is_eq and digit == digits[pos];
    }
    printf("Case #%d: %lld\n", tc, ans);
    DBG(tc);
  }
  return 0;
}

