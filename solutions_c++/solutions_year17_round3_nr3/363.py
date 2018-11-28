#include <bits/stdc++.h>

using namespace std;

int main() {
   int T;
   cin >> T;
   for(int testcase = 1; testcase <= T; testcase++) {
      int N, K;
      double U;
      cin >> N >> K >> U;
      vector<double> tab(N);
      for(int i = 0; i < N; ++i) cin >> tab[i];
      tab.push_back(1);
      sort(tab.begin(),tab.end());
      for(int i = 0; i < N; ++i) {
         double dist = tab[i+1] - tab[i];
         double to_add = min((i+1) * dist, U);
         dist = to_add / ((double) i+1);
         U -= to_add;
         for(int j = 0; j <= i; ++j) tab[j] += dist;
      }
      double sc = 1;
      for(double x : tab) sc *= x;
      cout << "Case #" << testcase << ": " << setprecision(18) << sc << endl;
   }
}
