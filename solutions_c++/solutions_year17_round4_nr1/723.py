#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <cmath>
#include <map>
#include <set>
#include <iomanip>
#define MOD 1000000007
#define EPS 1e-10
using namespace std;

void solve() {
   int n, p, g;
   int cnt[] = {0, 0, 0, 0, 0, 0};
   cin >> n >> p;
   for (int i = 0; i < n; i++) {
      cin >> g;
      cnt[g%p]++;
   }

   int ans = 0;
   ans += cnt[0];

   if (p == 2) {
      ans += (cnt[1]+1)/2;
   } else if (p == 3) {
      int tmp = min(cnt[1],cnt[2]);
      ans += tmp;
      cnt[1] -= tmp;
      cnt[2] -= tmp;
      ans += (cnt[1]+cnt[2]+2)/3;
   } else if (p == 4) {
      ans += (cnt[2]+1)/2;
      int tmp = min(cnt[1],cnt[3]);
      ans += tmp;
      cnt[1] -= tmp;
      cnt[3] -= tmp;
      ans += (cnt[1]+cnt[3]+3)/4;
   }

   cout << ans << endl;
}

int main() {
   int t, tc = 1;
   cin >> t;
   while (t--) {
      cout << "Case #" << tc++ << ": ";
      solve();
   }
}
