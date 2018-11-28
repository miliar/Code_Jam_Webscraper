#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <queue>
#include <deque>
#include <cassert>

// O = R + Y
// G = Y + B
// V = R + B


// R: B, Y, G
// Y: R, B, V
// B: Y, R, O
// O: B
// G: R
// V: Y

using namespace std;

const std::string impossible = "IMPOSSIBLE";

struct Char {
  char a, b;
  int n, m;
};

std::string solve() {
  int n, r, o, y, g, b, v;
  cin >> n >> r >> o >> y >> g >> b >> v;
  Char chars[3] = {{'B', 'O', b, o}, {'R', 'G', r, g}, {'Y', 'V', y, v}};
  sort(chars, chars+3, [](Char x, Char z){return x.n > z.n;});
  std::string res;
  for (Char& c: chars) {
    if (n - c.n - c.m == 0) {
      if (c.n != c.m)
        return impossible;
      for (int i=0;i<c.n;++i){
        res += c.a;
        res += c.b;
      }
      return res;
    }
    if (c.m && c.n <= c.m)
      return impossible;
    c.n -= c.m;
  }
  if (chars[0].n > chars[1].n + chars[2].n)
    return impossible;
  for (int i=0;i<chars[0].n;++i) {
    res += chars[0].a;
    while (chars[0].m-- > 0) {
      res += chars[0].b;
      res += chars[0].a;
    }
    if (i < chars[1].n) {
      res += chars[1].a;
      while (chars[1].m-- > 0) {
        res += chars[1].b;
        res += chars[1].a;
      }
    }
    int l = chars[1].n + chars[2].n - chars[0].n;
    if (i >= chars[1].n || i < l) {
      res += chars[2].a;
      while (chars[2].m-- > 0) {
        res += chars[2].b;
        res += chars[2].a;
      }
    }
  }
  return res;
}

int main() {
#ifdef LOCAL_RUN
  freopen("input.txt", "r", stdin);
#endif
  int t;
  cin >> t;
  for (int i=1;i<=t;++i) {
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}