#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

#define Loop(i, a, b) for (int i = (a); i < (b); ++i)

int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  //freopen("A-small-attempt0.in", "rt", stdin);
  freopen("A-large.in", "rt", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int line_num;
  cin >> line_num;
  for (int line = 1; line <= line_num; ++line) {
    char ch; string s; int k;
    cin >> s >> k;
    string str = "+" + s + "+";
    int n = s.size() + 1;
    VI vec(n);
    Loop(i, 0, n) {
      vec[i] = (str[i] != str[i+1]);
    }
    int ans = 0;
    Loop (i, 0, n - k) {
      if (vec[i]) {
        ans += 1;
        vec[i] = 0;
        vec[i + k] = 1 - vec[i + k];
      }
    }
    bool b = false;
    Loop (i, n - k, n) b = (b || vec[i]);
    if (!b)
      printf("Case #%d: %d\n", line, ans);
    else
      printf("Case #%d: %s\n", line, "IMPOSSIBLE");
  }

  return 0;
}
