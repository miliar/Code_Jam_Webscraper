#include <cstdio>
#include <vector>
#include <string>
#include <cassert>

using namespace std;

bool cmp(const int a, const int b) {
  if (a % 2 != b % 2) {
    return a % 2 == 0;
  }
  return a < b;
}

int main(void) {
  int T;
  int test_case = 1;
  scanf("%d", &T);

  while (T--) {
    int n;
  int r, y, b, o, g, v;
    scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
  
    if (r > y + b || y > b + r || b > r + y) {
      printf("Case #%d: IMPOSSIBLE\n", test_case++);
    } else {
      string s(n, 'x');

      vector<int> indices;
      for (int i = 0; i < n; ++i) {
        indices.push_back(i);
      }
      sort(indices.begin(), indices.end(), cmp);
      int iter = 0;

      vector<pair<int, char> > order;
      order.push_back(make_pair(r, 'R'));
      order.push_back(make_pair(y, 'Y'));
      order.push_back(make_pair(b, 'B'));
      sort(order.rbegin(), order.rend());

      for (int i = 0; i < order.size(); ++i) {
        int cnt = order[i].first;
        char c = order[i].second;
        while (cnt--) {
          s[indices[iter++]] = c;
        }
      }
      
      printf("Case #%d: %s\n", test_case++, s.c_str());

      for (int i = 0; i < n; ++i) {
        assert(!(s[(i - 1 + n) % n] == s[i] || s[(i + 1 + n) % n] == s[i]));
      }
    } 
  }
  return 0;
}
