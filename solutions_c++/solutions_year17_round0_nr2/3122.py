#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

typedef long long lol;
typedef vector<int> VI;
typedef vector<VI> VVI;

#define Loop(i, a, b) for (int i = (a); i < (b); ++i)
#define Loopb(i, a, b) for (int i = (a - 1); i >= (b); --i)

void find(lol n, VI &ret){
  while (n > 0) {
    ret.push_back(n % 10);
    n = n / 10;
  }
}

int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  //freopen("B-small-attempt3.in", "rt", stdin);
  freopen("B-large.in", "rt", stdin);
  freopen("outputB.txt", "w", stdout);
#endif

  int line_num;
  cin >> line_num;
  for (int line = 0; line < line_num; ++line) {
    lol n, ans = lol(0);
    cin >> n;
    VI vec;
    find(n, vec);
    bool b = false;
    int siz = vec.size();
      Loop (i, 0, siz - 1) if (vec[i] < vec[i+1]) b = true;
      if (!b) {
        ans = n;
      }  else {
        int st;
        Loopb (i, siz, 1) if (vec[i] > vec[i-1]) { st = i; break;}
        while ((st < siz - 1) && (vec[st] == vec[st + 1])) ++st;
        Loopb(i, siz, st) ans = 10 * ans + vec[i];
        --ans;
        Loop(i, 0, st) ans = 10* ans + 9;
      }
    printf("Case #%d: %ld\n", line+1, ans);
  }
  return 0;
}
