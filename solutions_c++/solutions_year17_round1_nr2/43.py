#include "bits/stdc++.h"
using namespace std;

const int N = 200;
const int MAGIC = 1000000;

int t, n, p, ans;
int arr[N];
int quantity[N][N];
int required[N];

int main() {
   freopen ("inp.in", "r", stdin);
   freopen ("C.out", "w", stdout);
   cin >> t;
   for (int qq = 1; qq <= t; qq++) {
      cin >> n >> p;
      for (int i = 1; i <= n; i++) {
         cin >> required[i];
      }
      for (int i = 1; i <= n; i++) {
         for (int j = 1; j <= p; j++) {
            cin >> quantity[i][j];
         }
         sort(quantity[i] + 1, quantity[i] + 1 + p);
      }
      ans = 0;
      for (int it = 1; (it <= MAGIC) && (p > 0); it++) {
         int id = 0;
         for (int i = 1; i <= n; i++) {
            int ql = 1, qr = p;
            while (ql < qr) {
               int mid = (ql + qr) / 2;
               if (quantity[i][mid] * 100 >= 90 * 1LL * it * required[i]) {
                  qr = mid;
               }
               else {
                  ql = mid + 1;
               }
            }
            if ((quantity[i][ql] * 100 >= 90 * 1LL * it * required[i]) && (
                  quantity[i][ql] * 100 <= 110 * 1LL * it * required[i])) {
               arr[id++] = ql;
            }
            else {
               break;
            }
         }
         if (id < n) {
            continue;
         }
         ans++;
         for (int i = 1; i <= n; i++) {
            swap(quantity[i][arr[i - 1]], quantity[i][p]);
            if (p > 1) {
               sort(quantity[i] + 1, quantity[i] + p);
            }
         }
         it--; p--;
      }
      cout << "Case #" << qq << ": " << ans << "\n";
   }
}