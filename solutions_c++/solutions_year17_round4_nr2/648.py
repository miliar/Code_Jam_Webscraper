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
   int n, c, m;
   cin >> n >> c >> m;
   int p, b;
   int cntseat[1001];
   int cntticket[1001];

   memset(cntseat, 0, sizeof cntseat);
   memset(cntticket, 0, sizeof cntticket);
   int ansmax = 0, ansupgrade = 0;

   for (int i = 0; i < m; i++) {
      cin >> p >> b;
      cntseat[p]++;
      cntticket[b]++;
      ansmax = max(ansmax, cntticket[b]);
   }

   int sum = 0;
   for (int i = 1; i <= n; i++) {
      sum += cntseat[i];
      if (sum > ansmax*i) {
         ansmax = (sum+i-1)/i;
      }
   }

   for (int i = 1; i <= n; i++) {
      if (cntseat[i] > ansmax) {
         ansupgrade += cntseat[i]-ansmax;
      }
   }

   cout << ansmax << ' ' << ansupgrade << endl;
}

int main() {
   int t, tc = 1;
   cin >> t;
   while (t--) {
      cout << "Case #" << tc++ << ": ";
      solve();
   }
}
