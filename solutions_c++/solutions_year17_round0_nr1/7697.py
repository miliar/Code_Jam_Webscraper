#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>

using namespace std;

#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define fup(i, a, b) for (__typeof(a) i = (a); i != (b); ++i)
#define fdown(i, a, b) for (__typeof(a) i = (a); i != (b); --i)
#define all(x) (x).begin(),(x).end()
#define forall(i, x) fup(i, (x).begin(),(x).end())
#define debug(x) cout << #x << " = " << x << "\n"

int main() {
  int t, c = 0;

  for (scanf("%d", &t); t--;) {
    string s;
    int k;

    cin >> s >> k;

    int count = 0;
    for (int i = 0; i <= (int)s.size()-k; ++i) {
      if (s[i] == '-') {
        ++count;
        for (int j = 0; j < k; ++j)
          s[i+j] = s[i+j] == '-' ? '+' : '-';
      }
    }

    bool ok = true;
    for (int i = 0; i < (int)s.size(); ++i)
      if (s[i] != '+')
        ok = false;

    printf("Case #%d: ", ++c);
    if (ok) printf("%d\n", count);
    else puts("IMPOSSIBLE");
  }

  return 0;
}
