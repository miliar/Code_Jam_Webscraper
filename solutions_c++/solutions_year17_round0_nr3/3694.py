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

long long n, k;

void solve() {
   cin >> n >> k;

   long long mor, les;
   long long morcnt, lescnt;
   morcnt = lescnt = 0;

   mor = n; les = n-1;
   morcnt = 1; lescnt = 0;

   long long i = 1;
   while (i*2 <= k) {
      int n_mor, n_les, n_morcnt, n_lescnt;
      n_morcnt = n_lescnt = 0;

      if (mor % 2 == 0) {
         n_mor = mor/2;
         n_les = n_mor-1;
         n_morcnt += morcnt; n_lescnt += morcnt;
         n_lescnt += lescnt*2;
      } else {
         n_mor = mor/2;
         n_les = n_mor-1;
         n_morcnt += morcnt*2;
         n_morcnt += lescnt; n_lescnt += lescnt;
      }

      i *= 2;
      mor = n_mor;
      les = n_les;
      morcnt = n_morcnt;
      lescnt = n_lescnt;

      //cout << mor << ' ' << morcnt << ' ' << les << ' ' << lescnt << endl;
   }

   k = (k-i+1);
   if (k <= morcnt)
      if (mor % 2 == 0) cout << mor/2 << ' ' << mor/2-1 << endl;
      else cout << mor/2 << ' ' << mor/2 << endl;
   else
      if (les % 2 == 0) cout << les/2 << ' ' << les/2-1 << endl;
      else cout << les/2 << ' ' << les/2 << endl;
}

int main() {
   int t; int tc = 1;
   cin >> t;
   while (t--) {
      cout << "Case #" << tc++ << ": ";
      solve();
   }
}
