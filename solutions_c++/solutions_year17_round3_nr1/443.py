#include <bits/stdc++.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;

double solution() {
   int n, k;
   cin >> n >> k;
   vector <double> dp(k + 1, 0);
   vector <pair <double, double>> ps(n);

   for (auto &x : ps) {
       cin >> x.first >> x.second;
   }

   sort(ps.begin(), ps.end());
   double max_square = 0;
   for (int i = 0; i < ps.size(); i++) {
      double prev = 0;
      for (int j = 1; j <= min((i + 1), k); j++) {
          double next_prev = dp[j];
          if (j == k) {
              max_square = max(max_square, prev + pi * ps[i].first * (ps[i].first + 2 * ps[i].second));
          }
          dp[j] = max(dp[j], prev + 2 * pi * ps[i].first * ps[i].second);
          prev = next_prev;
      }
   }
   return max_square;
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout.precision(20);
        cout << fixed;
        cout << "Case #" << test << ": " << solution() << '\n';
    }
    return 0;
}
