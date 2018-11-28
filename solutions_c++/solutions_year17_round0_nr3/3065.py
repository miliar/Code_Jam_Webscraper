#include <bits/stdc++.h>

using namespace std;

int main() {
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    long long n, k;
    cin >> n >> k;
    map <long long, long long> s;
    s[n] = 1LL;
    while (k > 0) {
      auto p = *(--s.end());
      s.erase(--s.end());
      long long len = p.first;
      long long cnt = p.second;
      if (cnt >= k) {
        cout << len / 2 << " " << (len - 1) / 2 << endl;
        break;
      }
      k -= cnt;
      s[len / 2] += cnt;
      s[(len - 1) / 2] += cnt;
    }
  }
  return 0;
}
