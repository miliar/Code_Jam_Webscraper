#include <bits/stdc++.h>
using namespace std;
#define lli long long int
#define li long int
template <class T>
T maxx(T a, T b) {
     if(a > b) {
          return a;
     }
     return b;
}
void solve() {
     double d, n, ans = 0, t1, t2;
     cin >> d >> n ;
     for(int i = 0; i < n; i++) {
          cin >> t1 >> t2;
          ans = maxx((double)(d - t1) / t2, (double)ans);
     }
     cout << setprecision(6) << fixed << d / ans << "\n";
}
int main() {
     int t;
     scanf("%d", &t);
     for(int i = 1; i <= t; i++) {
          cout << "Case #" << i << ": ";
          solve();
     }
     return 0;
}