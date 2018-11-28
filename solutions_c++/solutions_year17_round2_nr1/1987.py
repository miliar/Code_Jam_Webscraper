#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef long long lol;
typedef vector<int> VI;
typedef vector<VI> VVI;

#define Loop(i, a, b) for (int i = (a); i < (b); ++i)

bool letter(char ch) {return (ch >= 'A') && (ch <= 'Z');}

int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  //freopen("A-small-attempt1.in", "rt", stdin);
  freopen("A-large.in", "rt", stdin);
  freopen("outputA.txt", "w", stdout);
#endif

  int line_num;
  cin >> line_num;
  for (int line = 1; line <= line_num; ++line) {
    int n, m;
    cin >> m >> n;
    double ans = 0.000001, d = m;
    VI k(n), s(n);
    Loop(i, 0, n) {
      cin >> k[i] >> s[i];
      ans = max(ans, (d - k[i]) / s[i]);
    }
    ans = d / ans;
    printf("Case #%d: %.15f\n", line, ans);
  }

  return 0;
}
