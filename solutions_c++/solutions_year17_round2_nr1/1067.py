#include <bits/stdc++.h>

using namespace std;

int main() {
   int T;
   cin >> T;
   for(int test = 1; test <= T; test++) {
      double D;
      int N;
      cin >> D >> N;
      double min_time = 100000000000000;
      for(int i = 0; i < N; ++i) {
         double K, S;
         cin >> K >> S;
         min_time = min(min_time, D / ((D - K) / S));
      }
      cout << "Case #" << setprecision(18) << test << ": " << min_time << endl;
   }
}
