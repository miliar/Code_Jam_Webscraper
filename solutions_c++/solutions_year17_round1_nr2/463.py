#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <cmath>
#include <map>
#include <set>
#define MOD 1000000007
using namespace std;

int n, p;
vector<long long> r;
vector< vector<long long> > q;
vector<int> idx;

bool isSet() {
   /*cout << "checking ";
   for (int i = 0; i < n; i++)
      cout << q[i][idx[i]] << ' ';
   cout << endl;*/

   int lo = 1;
   int hi = 1000000;
   while (lo <= hi) {
      int mid = (lo+hi)/2;
      bool isGood = true;
      for (int i = 0; i < n; i++) {
         double good90 = 0.9*mid*r[i];
         double good110 = 1.1*mid*r[i];
         double can = q[i][idx[i]];
         if (good90 <= can && can <= good110) continue;
         else if (can < good90) { hi = mid-1; isGood = false; break; }
         else if (can > good110) { lo = mid+1; isGood = false; break; }
      }
      if (isGood) return true;
   }
   return false;
}

void solve() {
   cin >> n >> p;
   r.assign(n, 0);
   q.assign(n, vector<long long>(p, 0));
   idx.assign(n, 0);

   for (int i = 0; i < n; i++) cin >> r[i];
   for (int i = 0; i < n; i++)
      for (int j = 0; j < p; j++)
         cin >> q[i][j];
   for (int i = 0; i < n; i++) sort(q[i].begin(), q[i].end());

   int ans = 0;
   while (true) {
      if (isSet()) {
         bool isBreak = false;
         for (int i = 0; i < n; i++) {
            idx[i]++;
            if (idx[i] >= p) isBreak = true;
         }
         ans++;
         if (isBreak) break;
      } else {
         int minIdx = 0;
         double minDbl = q[0][idx[0]]/r[0];
         for (int i = 0; i < n; i++) {
            double tmp = q[i][idx[i]]/r[i];
            if (minDbl > tmp) {
               minIdx = i;
               minDbl = tmp;
            }
         }
         idx[minIdx]++;
         if (idx[minIdx] >= p) break;
      }
   }
   cout << ans << endl;
}

int main() {
   int t; int tc = 1;
   cin >> t;
   while (t--) {
      cout << "Case #" << tc++ << ": ";
      solve();
   }
}
